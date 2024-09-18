import cv2
import mediapipe as mp
import time
import vkey  # Assuming you have a module for virtual keypresses

# Initialize MediaPipe holistic model
mp_holistic = mp.solutions.holistic
mp_drawing = mp.solutions.drawing_utils

# Initialize video capture
videoCap = cv2.VideoCapture(0)

# Initialize action timestamps
last_volume_action_time = 0
last_track_action_time = 0
last_playpause_action_time = 0
action_delay = 0.5  # Delay in seconds

# Function to recognize basic gestures based on hand landmarks
def recognize_gesture(hand_landmarks, img_width, img_height):
    thumb_tip = hand_landmarks.landmark[mp_holistic.HandLandmark.THUMB_TIP]
    thumb_mcp = hand_landmarks.landmark[mp_holistic.HandLandmark.THUMB_CMC]
    index_tip = hand_landmarks.landmark[mp_holistic.HandLandmark.INDEX_FINGER_TIP]
    index_mcp = hand_landmarks.landmark[mp_holistic.HandLandmark.INDEX_FINGER_MCP]
    middle_tip = hand_landmarks.landmark[mp_holistic.HandLandmark.MIDDLE_FINGER_TIP]
    middle_mcp = hand_landmarks.landmark[mp_holistic.HandLandmark.MIDDLE_FINGER_MCP]
    ring_tip = hand_landmarks.landmark[mp_holistic.HandLandmark.RING_FINGER_TIP]
    ring_mcp = hand_landmarks.landmark[mp_holistic.HandLandmark.RING_FINGER_MCP]
    pinky_tip = hand_landmarks.landmark[mp_holistic.HandLandmark.PINKY_TIP]
    pinky_mcp = hand_landmarks.landmark[mp_holistic.HandLandmark.PINKY_MCP]

    # Convert to pixel coordinates
    thumb_tip_x = int(thumb_tip.x * img_width)
    thumb_tip_y = int(thumb_tip.y * img_height)
    thumb_mcp_x = int(thumb_mcp.x * img_width)
    thumb_mcp_y = int(thumb_mcp.y * img_height)    
    index_tip_x = int(index_tip.x * img_width)
    index_tip_y = int(index_tip.y * img_height)
    middle_tip_y = int(middle_tip.y * img_height)
    ring_tip_y = int(ring_tip.y * img_height)
    pinky_tip_y = int(pinky_tip.y * img_height)
    ring_mcp_y = int(ring_mcp.y * img_height)
    pinky_mcp_y = int(pinky_mcp.y * img_height)

    # Thumbs Up: thumb is above its MCP joint and higher than the index finger
    if thumb_tip_y < thumb_mcp_y and thumb_tip_y < index_tip_y:
        return "thumb_up"

    # Thumbs Down: thumb is below its MCP joint and lower than the index finger
    if thumb_tip_y > thumb_mcp_y and thumb_tip_y > index_tip_y:
        return "thumb_down"

    # Peace sign: Index and middle fingers up, ring and pinky down
    if (index_tip_y < thumb_tip_y and middle_tip_y < thumb_tip_y and 
        ring_tip_y > middle_tip_y and pinky_tip_y > ring_tip_y):
        return "peace"

    # OK sign: Thumb and index finger tips close to each other
    if abs(thumb_tip.x - index_tip.x) < 20 and abs(thumb_tip.y - index_tip.y) < 20:
        return "ok_sign"

    # Open palm: All fingers spread out
    if (thumb_tip_y < thumb_mcp_y and
        index_tip_y < middle_tip_y and 
        middle_tip_y < ring_tip_y and ring_tip_y < pinky_tip_y):
        return "open_palm"

    return None

with mp_holistic.Holistic(min_detection_confidence=0.7, min_tracking_confidence=0.7) as holistic:
    while videoCap.isOpened():
        ret, frame = videoCap.read()

        if not ret:
            break

        # Convert the frame to RGB (MediaPipe uses RGB)
        imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame to get landmarks
        results = holistic.process(imgRGB)

        # Extract the dimensions of the frame
        img_height, img_width, _ = frame.shape

        gesture_right = None
        gesture_left = None

        # Draw landmarks and recognize gestures for right hand
        if results.right_hand_landmarks:
            mp_drawing.draw_landmarks(frame, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
            gesture_right = recognize_gesture(results.right_hand_landmarks, img_width, img_height)

            # Perform actions based on right hand gestures with delay
            current_time = time.time()
            if gesture_right == "thumb_up" and (current_time - last_volume_action_time) > action_delay:
                last_volume_action_time = current_time
                vkey.volume_up_press()
            elif gesture_right == "thumb_down" and (current_time - last_volume_action_time) > action_delay:
                last_volume_action_time = current_time
                vkey.volume_down_press()

        # Draw landmarks and recognize gestures for left hand
        if results.left_hand_landmarks:
            mp_drawing.draw_landmarks(frame, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
            gesture_left = recognize_gesture(results.left_hand_landmarks, img_width, img_height)

            # Perform actions based on left hand gestures with delay
            current_time = time.time()
            if gesture_left == "thumb_up" and (current_time - last_track_action_time) > action_delay:
                last_track_action_time = current_time
                vkey.next_press()
            elif gesture_left == "thumb_down" and (current_time - last_track_action_time) > action_delay:
                last_track_action_time = current_time
                vkey.previous_press()

        # Detect two peace signs
        if gesture_right == "peace" and gesture_left == "peace":
            current_time = time.time()
            if (current_time - last_playpause_action_time) > action_delay:
                last_playpause_action_time = current_time
                vkey.playpause_press()

        # Display recognized gestures on the screen
        if gesture_right:
            cv2.putText(frame, f'Right Hand Gesture: {gesture_right}', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        if gesture_left:
            cv2.putText(frame, f'Left Hand Gesture: {gesture_left}', (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Display the frame
        cv2.imshow('Holistic Model', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

videoCap.release()
cv2.destroyAllWindows()
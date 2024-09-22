import cv2
import mediapipe as mp
import time
import tensorflow as tf
import numpy as np
import vkey  # Assuming you have a module for virtual keypresses
import csv

# Load TensorFlow Lite model
interpreter = tf.lite.Interpreter(model_path="models/keypoint_classifier.tflite")
interpreter.allocate_tensors()

# Get input and output tensors
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Load gesture labels from CSV
with open("models/keypoint_classifier_label.csv", encoding='utf-8-sig') as f:
    gesture_labels = [row[0] for row in csv.reader(f)]

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

# Function to preprocess hand landmarks for model input
def preprocess_landmarks(landmarks, img_width, img_height):
    # Convert hand landmarks to a flat list
    hand_points = np.array([[lm.x * img_width, lm.y * img_height] for lm in landmarks.landmark], dtype=np.float32)
    hand_points = hand_points.flatten()  # Flatten the 2D array to 1D
    return hand_points

# Function to predict gesture using the TFLite model
def predict_gesture(landmarks, img_width, img_height):
    input_data = np.expand_dims(preprocess_landmarks(landmarks, img_width, img_height), axis=0).astype(np.float32)
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]['index'])
    predicted_label = np.argmax(output_data)
    return gesture_labels[predicted_label]

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

        # Draw landmarks and predict gestures for right hand
        if results.right_hand_landmarks:
            mp_drawing.draw_landmarks(frame, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
            gesture_right = predict_gesture(results.right_hand_landmarks, img_width, img_height)

            # Perform actions based on right hand gestures with delay
            current_time = time.time()
            if gesture_right == "thumb_up" and (current_time - last_volume_action_time) > action_delay:
                last_volume_action_time = current_time
                vkey.volume_up_press()
            elif gesture_right == "thumb_down" and (current_time - last_volume_action_time) > action_delay:
                last_volume_action_time = current_time
                vkey.volume_down_press()

        # Draw landmarks and predict gestures for left hand
        if results.left_hand_landmarks:
            mp_drawing.draw_landmarks(frame, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
            gesture_left = predict_gesture(results.left_hand_landmarks, img_width, img_height)

            # Perform actions based on left hand gestures with delay
            current_time = time.time()
            if gesture_left == "thumb_up" and (current_time - last_track_action_time) > action_delay:
                last_track_action_time = current_time
                vkey.next_press()
            elif gesture_left == "thumb_down" and (current_time - last_track_action_time) > action_delay:
                last_track_action_time = current_time
                vkey.previous_press()

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
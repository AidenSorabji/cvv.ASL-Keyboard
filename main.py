# -------------------- Imports --------------------  #
# Mediapipe for hand tracking and other ML tasks
import mediapipe as mp

# OpenCV for video capture and image processing
import cv2

# Pynput for controlling keyboard (although it's not used here)
from pynput.keyboard import Controller, Key

# Utilities for time measurement and system commands
import time
from subprocess import call
import numpy as np  # For numerical operations (e.g., minimum, maximum calculations)

import handtrackingmodule as htm

# Constants for hand landmarks and volume control
INDEX_FINGER_IDX = 8  # Index for the tip of the index finger in MediaPipe hand tracking
THUMB_IDX = 4         # Index for the thumb tip in MediaPipe hand tracking
VOLUME_UPDATE_INTERVAL = 15  # Adjust volume every 15 frames

# Open the default camera (0 represents the default camera)
videoCap = cv2.VideoCapture(0)

# Variables for frame timing and distance calculations
lastFrameTime = 0  # Time of the previous frame (used to calculate FPS)
frame = 0          # Frame counter
max_diff = 0       # Maximum distance between thumb and index finger (for volume normalization)
min_diff = 100000  # Minimum distance between thumb and index finger (for volume normalization)

# Setup MediaPipe hand tracking solution
handSolution = mp.solutions.hands
hands = handSolution.Hands()

detector = htm.HandDetector(detectionCon=0.7) 
numberOfFingers = 0

# Main loop to capture and process frames
while True:
    frame += 1  # Increment the frame counter

    # Capture a frame from the camera
    success, img = videoCap.read()

    # If frame capture was successful, process the image
    if success:
        # Convert the image from BGR (OpenCV format) to RGB (required by MediaPipe)
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Calculate FPS (frames per second)
        thisFrameTime = time.time()  # Get the current time
        fps = 1 / (thisFrameTime - lastFrameTime)  # FPS = 1 / time difference between frames
        lastFrameTime = thisFrameTime  # Update the last frame time for the next iteration

        # Overlay the FPS value on the image
        cv2.putText(img, f'FPS:{int(fps)}', (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Process the image to detect hands
        recHands = hands.process(imgRGB)

        # If hands are detected, process each detected hand
        if recHands.multi_hand_landmarks:
            for hand in recHands.multi_hand_landmarks:
                # For each landmark in the hand, draw a circle on the image
                for datapoint_id, point in enumerate(hand.landmark):
                    h, w, c = img.shape  # Get the height, width, and channels of the image
                    x, y = int(point.x * w), int(point.y * h)  # Convert normalized coordinates to pixel values
                    cv2.circle(img, (x, y), 10, (255, 0, 255), cv2.FILLED)  # Draw a circle at each landmark point

                fingers_up = []

                # Check if the thumb is up (compare thumb tip (4) with thumb IP joint (3))
                if is_finger_up(hand.landmark[4], hand.landmark[3], h):
                    fingers_up.append("Thumb")
                if is_finger_up(hand.landmark[8], hand.landmark[7], h):
                    fingers_up.append("Index")
                if is_finger_up(hand.landmark[12], hand.landmark[11], h):
                    fingers_up.append("Middle")
                if is_finger_up(hand.landmark[16], hand.landmark[15], h):
                    fingers_up.append("Ring")
                if is_finger_up(hand.landmark[20], hand.landmark[19], h):
                    fingers_up.append("Pinky")
                
                # Print the number of fingers up and which ones in the terminal
                print(f"Fingers up: {len(fingers_up)} -> {', '.join(fingers_up)}")

            # Update volume every VOLUME_UPDATE_INTERVAL frames
            if frame % VOLUME_UPDATE_INTERVAL == 0:
                thumb_y = hand.landmark[THUMB_IDX].y  # Y-coordinate of the thumb tip
                index_y = hand.landmark[INDEX_FINGER_IDX].y  # Y-coordinate of the index finger tip

                # Calculate the distance between the thumb and index finger (in pixels)
                distance = thumb_y * h - index_y * h

                # Adjust min_diff and max_diff for calibration
                min_diff = np.minimum(distance + 50, min_diff)  # Calibrate min distance with buffer
                max_diff = np.maximum(distance, max_diff)  # Calibrate max distance

                # Adjust the system volume on macOS based on the finger distance
                # Volume is normalized between 0 and 100 using the distance between thumb and index finger
                call(["osascript -e 'set volume output volume {}'"
                      .format(np.clip(
                          (distance / (max_diff - min_diff) * 100),  # Calculate the volume percentage
                          0, 100))], shell=True)  # Clip the value between 0 and 100

                frame = 0  # Reset the frame counter after updating volume

        # Display the image in a window called "CamOutput"
        cv2.imshow("CamOutput", img)

        # Wait 1 millisecond for a key press (allows for smooth video display)
        cv2.waitKey(1)
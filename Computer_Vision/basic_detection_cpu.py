#Completely vibe coded computer vision funcitnality for the presentation haha
# Will come back to learn this from scratch next sem 

import cv2
import mediapipe as mp
from ultralytics import YOLO


# --- 1. INITIALIZE MODELS ---
# MediaPipe for CPU-optimized Face Detection
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils
face_detector = mp_face_detection.FaceDetection(min_detection_confidence=0.5)


# YOLO for Weapons (Load your downloaded model here)
# Note: If you convert this to OpenVINO, point to the newly created folder instead of the .pt file
weapon_model = YOLO('models/yolov8n.pt') 


# --- 2. SETUP VIDEO STREAM ---
# Replace 0 with your drone's video stream URL or IP if needed
cap = cv2.VideoCapture(0)


# --- 3. OPTIMIZATION VARIABLES ---
frame_skip_rate = 3  # Only run YOLO every 3rd frame
frame_count = 0
latest_weapon_results = None # Stores the bounding boxes to draw on skipped frames


while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Stream ended or failed.")
        break
        
    # OPTIMIZATION: Downscale the frame to save CPU processing power
    frame = cv2.resize(frame, (640, 480))

    # --- FAST PATH: FACE DETECTION (Runs every frame) ---
    # MediaPipe requires RGB format
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_results = face_detector.process(rgb_frame)
    
    if face_results.detections:
        for detection in face_results.detections:
            mp_drawing.draw_detection(frame, detection)

    # --- HEAVY PATH: WEAPON DETECTION (Runs every Nth frame) ---
    if frame_count % frame_skip_rate == 0:
        # Run YOLO inference. verbose=False stops it from spamming your terminal
        latest_weapon_results = weapon_model(frame, conf=0.4, verbose=False)
        
    # Draw the latest known weapon bounding boxes onto the current frame
    if latest_weapon_results:
        # plot() automatically draws the boxes and labels onto the image
        frame = latest_weapon_results[0].plot(img=frame)

    # Show the final optimized feed
    cv2.imshow("Surveillance Drone - CPU Optimized Feed", frame)
    frame_count += 1

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# Cleanup
cap.release()
cv2.destroyAllWindows()
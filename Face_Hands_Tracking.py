import cv2
import mediapipe as mp
import time
import pygame


def is_x_gesture(left_hand, right_hand):
    tips = [4, 8, 12, 16, 20]
    joints = [3, 6, 10, 14, 18]

    fingers = 0

    if left_hand:
        for tip, joint in zip(tips, joints):
            if left_hand.landmark[tip].y < left_hand.landmark[joint].y:
                fingers += 1

    if right_hand:
        for tip, joint in zip(tips, joints):
            if right_hand.landmark[tip].y < right_hand.landmark[joint].y:
                fingers += 1

    return fingers


cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands.Hands(static_image_mode=False,max_num_hands=2, min_detection_confidence=0.5,min_tracking_confidence=0.5)

mp_face = mp.solutions.face_detection
face_detection = mp_face.FaceDetection(
    model_selection=0,
    min_detection_confidence=0.5
)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results_hands = mp_hands.process(imgRGB)
    results_face = face_detection.process(imgRGB)
    if not ret:
        print("Error with camera")
        break


    left_hand = None
    right_hand = None

    if results_hands.multi_hand_landmarks:
        for hand_landmarks, handedness in zip(
            results_hands.multi_hand_landmarks,
            results_hands.multi_handedness
        ):
            label = handedness.classification[0].label  # "Left" or "Right"

            if label == "Left":
                left_hand = hand_landmarks
            else:
                right_hand = hand_landmarks

            mp.solutions.drawing_utils.draw_landmarks(
                frame, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS
            )

    fingers = is_x_gesture(left_hand, right_hand)

    cv2.putText(frame,
            f"Fingers: {fingers}",
            (50,200),
            cv2.FONT_HERSHEY_SIMPLEX,
            2,
            (255,0,0),
            6)

    if results_face.detections:
        for detection in results_face.detections:
            mp.solutions.drawing_utils.draw_detection(frame, detection)
        cv2.putText(frame, "Face Detected!!!", (50,50),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),6)
    cv2.imshow("Camera", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



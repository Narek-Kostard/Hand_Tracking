import cv2
import mediapipe as mp
import pygame
pygame.mixer.init()
pygame.mixer.music.load(r"PATH/TO/SOUND.mp3")


def is_x_gesture(hand_landmarks):
    tips = [4, 8, 12, 16, 20]
    joints = [3, 6, 10, 14, 18]

    folded = 0

    for tip, joint in zip(tips[1:], joints[1:]):
        if hand_landmarks.landmark[tip].y > hand_landmarks.landmark[joint].y:
            folded += 1


    thumb_extended = hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x

    if folded == 4 and thumb_extended:
        return True
    else:
        return False



cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands.Hands(static_image_mode=False,max_num_hands=2, min_detection_confidence=0.5,min_tracking_confidence=0.5)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = mp_hands.process(imgRGB)

    if not ret:
        print("Error with camera")
        break




    if mp_hands.process(imgRGB).multi_hand_landmarks:
        for hand in results.multi_hand_landmarks:
            mp.solutions.drawing_utils.draw_landmarks(
                frame, hand, mp.solutions.hands.HAND_CONNECTIONS
            )
            if is_x_gesture(hand):
                pygame.mixer.music.play()
            
    cv2.imshow("Camera", frame)
    if cv2.waitKey(1) == ord('q'):
        break


    
cap.release()
cv2.destroyAllWindows()






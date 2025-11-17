# Hand & Face Detector with Finger Counter ✋👀

A real-time computer vision application using **MediaPipe** and **OpenCV** that:
- Detects and tracks up to 2 hands
- Determines hand laterality (Left / Right)
- Counts how many fingers are extended (raised above the finger joints)
- Detects faces in the frame
- Displays live feedback on screen

Perfect for gesture recognition prototypes, accessibility tools, or just having fun with hand tracking!

## Features
- Real-time hand landmark detection using MediaPipe Hands
- Accurate left/right hand classification
- Finger extension detection (counts raised fingers across both hands)
- Face detection using MediaPipe Face Detection
- Visual feedback: landmarks, bounding boxes, and on-screen counters
- Simple and lightweight — runs smoothly on most laptops with a webcam

## Requirements

- Python 3.7+
- OpenCV
- MediaPipe
- pygame (currently imported but not used — can be removed if desired)
You have to download python 3.12.0 (Windows) or python 3.10.0 (MacOS)

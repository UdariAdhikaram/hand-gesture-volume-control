import cv2
import mediapipe as mp
import pyautogui
webcam = cv2.VideoCapture(0)
while True:
    _ , image = webcam.read()
    cv2.imshow("Hand volume control using python", image)
    key = cv2.waitKey(10)
    if key == 27:
        break
webcam.release()
cv2.destroyAllWindows()
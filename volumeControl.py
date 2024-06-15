import cv2
import mediapipe as mp
import pyautogui
webcam = cv2.VideoCapture(0)
while True:
    _ , image = webcam.read()
    image = cv2.flip(image,1)
        dist = ((x2-x1)**2 + (y2-y1)**2)**(0.5)//4
        if dist > 50 :
            pyautogui.press("volumeup")
        else :
            pyautogui.press("volumedown")

    cv2.imshow("Hand volume control using python", image)
    key = cv2.waitKey(10)
    if key == 27:
        break
webcam.release()
cv2.destroyAllWindows()
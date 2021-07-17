import numpy as nu
import cv2
import pyautogui


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
cap = cv2.VideoCapture(0)
u = 0
d = 0
l = 0
r = 0

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        if y < 150:
            if u % 5 == 0:
                pyautogui.press('up')
                print('U')
            u += 1

        elif y > 250:
            if d % 5 == 0:
                pyautogui.press('down')
                print('D')
            d += 1

        elif x < 100:
            if r % 15 == 0:
                pyautogui.press('right')
                print('R')
            r += 1

        elif x > 300:
            if l % 15 == 0:
                pyautogui.press('left')
                print('L')
            l += 1

    cv2.imshow('frame', frame)
    if cv2.waitKey(10) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
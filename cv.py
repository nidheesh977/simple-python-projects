import cv2

cap = cv2.VideoCapture(0)

yellow_lower = np.array([0, 70, 50])
yellow_upper = np.array([10, 255, 255])
u = 0
d = 0
l = 0
r = 0

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, yellow_lower, yellow_upper)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        area = cv2.contourArea(c)
        if area > 1000:
            x, y, w, h = cv2.boundingRect(c)
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

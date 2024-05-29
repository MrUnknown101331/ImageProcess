import cv2
import time
import numpy
from screeninfo import get_monitors
from pynput.mouse import Button, Controller
from HandTrackingModule import HandDetector

wCam, hCam = 640, 480
p_time = 0
frameR = 120
shiftUp = 60
smoothFactor = 8
pLocX, pLocY = 0, 0
clicked = False

detector = HandDetector(max_hands=1, track_conf=0.7)
mouse = Controller()
monitors = get_monitors()
wScreen, hScreen = monitors[0].width, monitors[0].height

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    lmList, img = detector.find_position(img)

    if lmList:
        cv2.rectangle(img, (frameR, frameR - shiftUp), (wCam - frameR, hCam - frameR - shiftUp), (255, 0, 255), 2)
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
        fingers = detector.fingers_up(lmList)
        if fingers[3] == 0:
            if fingers[1] == 1 and fingers[0] == 0:
                x3 = numpy.interp(x1, (frameR, wCam - frameR - shiftUp), (0, wScreen))
                y3 = numpy.interp(y1, (frameR, hCam - frameR - shiftUp), (0, hScreen))
                cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)

                cLocX = pLocX + (x3 - pLocX) / smoothFactor
                cLocY = pLocY + (y3 - pLocY) / smoothFactor
                mouse.position = (cLocX, cLocY)
                pLocX, pLocY = cLocX, cLocY

            if fingers[1] == 1 and fingers[0] == 1:
                dist, img, points = detector.find_distance(4, 8, img, lmList)
                if dist <= 35:
                    cv2.circle(img, (points[4], points[5]), 15, (0, 255, 0), cv2.FILLED)
                    if not clicked:
                        mouse.click(Button.left)
                        clicked = True
                else:
                    if clicked:
                        clicked = False

    c_time = time.time()
    fps = 1 / (c_time - p_time)
    p_time = c_time
    cv2.putText(img, f'{int(fps)}FPS', (10, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1)

    cv2.imshow("Image", img)
    cv2.waitKey(1)

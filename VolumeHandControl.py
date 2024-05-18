import cv2
import numpy
import time
from HandTrackingModule import HandDetector
import math
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

pTime = 0
cap = cv2.VideoCapture(0)
detector = HandDetector(track_conf=0.7)
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
vRange = volume.GetVolumeRange()  # (-96.0, 0.0)
while True:
    success, img = cap.read()
    l_mark_list, img = detector.find_position(img)

    if l_mark_list:
        x1, y1 = l_mark_list[4][1], l_mark_list[4][2]
        x2, y2 = l_mark_list[8][1], l_mark_list[8][2]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        dist = math.hypot((x2 - x1), (y2 - y1))

        if dist < 50:
            color = (0, 255, 0)
        else:
            color = (255, 0, 25)

        cv2.line(img, (x1, y1), (x2, y2), (200, 0, 150), 3)
        cv2.circle(img, (x1, y1), 10, (255, 0, 138), cv2.FILLED)
        cv2.circle(img, (x2, y2), 10, (255, 0, 138), cv2.FILLED)
        cv2.circle(img, (cx, cy), 7, color, cv2.FILLED)

        vol = numpy.interp(dist, [50, 150], [vRange[0], vRange[1]])
        volume.SetMasterVolumeLevel(vol, None)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    per = numpy.interp(volume.GetMasterVolumeLevel(), [vRange[0], vRange[1]], [0, 100])
    cv2.putText(img, f'{int(fps)}FPS', (10, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1)
    cv2.putText(img, f'{int(per)}%', (10, 80), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1)

    cv2.imshow("Image", img)
    cv2.waitKey(1)

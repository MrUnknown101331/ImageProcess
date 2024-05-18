import cv2
import mediapipe as mp
import time


class HandDetector:
    def __init__(self, static_mode=False, max_hands=2, complexity=1, detect_conf=0.5, track_conf=0.5):
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(static_mode, max_hands, complexity, detect_conf, track_conf)
        self.mpDraw = mp.solutions.drawing_utils
        self.tipIds = [4, 8, 12, 16, 20]

    def find_hands(self, image, draw=True):
        img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = self.hands.process(img_rgb)

        if results.multi_hand_landmarks:
            for handLandMarks in results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(image, handLandMarks, self.mpHands.HAND_CONNECTIONS)
        return results, image

    def find_position(self, image, hand_no=0, draw=True):
        lm_list = []
        results, image = HandDetector.find_hands(self, image, draw)
        if results.multi_hand_landmarks and len(results.multi_hand_landmarks) > hand_no:
            my_hand = results.multi_hand_landmarks[hand_no]
            for pid, lm in enumerate(my_hand.landmark):
                h, w, c = image.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lm_list.append([pid, cx, cy])
        return lm_list, image

    def fingers_up(self, lm_list):
        fingers = []
        # Thumb
        if lm_list[self.tipIds[0]][1] > lm_list[self.tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        # Fingers
        for f_id in range(1, 5):
            if lm_list[self.tipIds[f_id]][2] < lm_list[self.tipIds[f_id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        return fingers


if __name__ == "__main__":
    p_time = 0
    c_time = 0
    cap = cv2.VideoCapture(0)
    detector = HandDetector()
    while True:
        success, img = cap.read()
        l_mark_list, img = detector.find_position(img, hand_no=1)

        if l_mark_list:
            l_mark = l_mark_list[4]
            cv2.circle(img, (l_mark[1], l_mark[2]), 15, (255, 0, 255), cv2.FILLED)

        c_time = time.time()
        fps = 1 / (c_time - p_time)
        p_time = c_time
        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_DUPLEX, 2, (255, 5, 255), 2)

        cv2.imshow("Image", img)
        cv2.waitKey(1)

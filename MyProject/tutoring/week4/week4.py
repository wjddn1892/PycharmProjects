# 카메라를 띄우고 회색화면을 반으로 줄이고
# 화면 가운데에 박스를 나타내는 코드

# import cv2
# import numpy as np
#
# cap = cv2.VideoCapture(0)
#
# while True:
#         ret, frame = cap.read()
#
#         if ret:
#                 shrink = cv2.resize(frame, None, fx=0.5, fy=0.5)
#                 gray = cv2.cvtColor(shrink, cv2.COLOR_BGR2GRAY)
#
#                 cv2.rectangle(gray, (110, 70), (210, 170), (0, 255, 0), 3)
#                 cv2.imshow('gray', gray)
#
#         if cv2.waitKey(1) & 0xff == ord('q'):
#                 break
#
# cv2.destroyAllWindows()
# cap.release()
#
# ###############################
# # 얼굴인식
#
# import cv2
#
# cap = cv2.VideoCapture(0)
# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#
# while True:
#         ret, img = cap.read()
#
#         if ret:
#
#                 gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#                 faces = face_cascade.detectMultiScale(gray, 1.1, 4)
#
#                 # faces = [(x1, y1, w1, h1), (x2, y2, w2, h2)]
#
#                 for (x, y, w, h) in faces:
#                         cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
#
#                 cv2.imshow('img', img)
#
#         if cv2.waitKey(1) & 0xff == ord('q'):
#                 break
#
# cv2.destroyAllWindows()
# cap.release()

##################################
# smile detection

import cv2
import time

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

def detect(gray, frame):
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), ((x + w), (y + h)), (255, 0, 0), 2)

        # roi = range of interest
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 20)

        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(roi_color, (sx, sy), ((sx + sw), (sy + sh)), (0, 0, 255), 2)

        ########## image save ###########
        if len(smiles) > 0:
                timestamp = int(time.time())  # 시간에 대한 함수
                cv2.imwrite('{}.jpg'.format(timestamp), frame)  # 웃는 얼굴이 인식될 때마다 사진 저장
        #################################

    return frame


while True:
        ret, img = cap.read()

        if ret:

                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.1, 4)

                canvas = detect(gray, img)

                cv2.imshow('Video', canvas)



        if cv2.waitKey(1) & 0xff == ord('q'):
                break

cv2.destroyAllWindows()
cap.release()

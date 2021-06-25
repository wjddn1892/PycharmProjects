import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    if ret:                          #####
        cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
            break

cv2.destroyAllWindows()
cap.release()

#외우기

###########################################

import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()

    if ret == True:                #####
        cv2.imshow('frame', img)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()

#외우기

###########################


import cv2
import numpy as np          #numpy는 행렬 불러올때 필요함

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()

    if ret:
        cv2.imshow('frame', img)
        print(img[100][100])

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()

##########################

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()

    if ret:
        cv2.imshow('frame', img)
        
        roi = img[100:200, 100:200]

        cv2.imshow('roi', roi)
        
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()

##################################

import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()

    if ret:
        cv2.imshow('img', img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        cv2.imshow('gray',gray)
        ret, thresh1 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()

############################

import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()

    if ret:
        cv2.imshow('img', img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        cv2.imshow('gray', gray)
        _, thresh1 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        
        shrink1 = cv2.resize(gray, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
        cv2.imshow('shrink1',shrink1)

        shrink2 = cv2.resize(gray, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
        cv2.imshow('shrink2',shrink2)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()

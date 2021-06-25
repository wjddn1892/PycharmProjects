import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()

    if ret:
        cv2.imshow('frame', img)

        # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # shrink = cv2.resize(img, None, fx=0.3, fy=0.3, interpolation=cv2.INTER_AREA)
        # area = img[100:200, 100:200]
        # img[100:300, 100:300] = np.zeros(shape=(200, 200, 3))
        # print(img[100][100])
        # print(img.shape)
        # print(gray.shape)
        #
        # _, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
        # _, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
        #
        # cv2.imshow('thresh1', thresh1)
        # cv2.imshow('thresh2', thresh2)
        # cv2.imshow('gray', gray)
        # cv2.imshow('shrink', shrink)


        if cv2.waitKey(1) & 0xff == ord('q'):
            break



cv2.destroyAllWindows()
cap.release()

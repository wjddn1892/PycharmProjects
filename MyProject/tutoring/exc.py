import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if ret:
        gray = cv2.resize(frame, None, fx=0.5, fy=0.5)

        cv2.rectangle(gray, (110, 70), (210, 170), (255, 255, 255), 3)
        cv2.imshow('gray', gray)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()

import numpy as np
import cv2 as cv

# read webcam using cv
cap = cv.VideoCapture(0)

# if cap.isOpened():
#     ret, frame = cap.read()
# else:
#     ret = False
# while ret:
#     ret, frame = cap.read()
#     cv.imshow("webcam", frame)
#     if cv.waitKey(25) & 0xFF ==ord("q"):
#         break

# cap.release()
# cv.destroyAllWindows()


# change the cam into grayscale
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    gray_image = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow("Grayscale camera", gray_image)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv.destroyAllWindows()
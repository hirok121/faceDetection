import cv2 as cv
import numpy as np
import os
import time


webcam=cv.VideoCapture(0)
# webcam.set(cv.CAP_PROP_FRAME_WIDTH, 640)
# webcam.set(cv.CAP_PROP_FRAME_HEIGHT, 480)
# webcam.set(cv.CAP_PROP_FPS, 30)
# webcam.set(cv.CAP_PROP_BRIGHTNESS, 0.5)
# webcam.set(cv.CAP_PROP_CONTRAST, 0.5)
# webcam.set(cv.CAP_PROP_SATURATION, 0.5)
# webcam.set(cv.CAP_PROP_HUE, 0.5)
# webcam.set(cv.CAP_PROP_GAIN, 0.5)
# webcam.set(cv.CAP_PROP_EXPOSURE, 0.5)
# # webcam.set(cv.CAP_PROP_WHITE_BALANCE, 0.5)
# webcam.set(cv.CAP_PROP_BACKLIGHT, 0.5)
# webcam.set(cv.CAP_PROP_ZOOM, 0.5)
# webcam.set(cv.CAP_PROP_FOCUS, 0.5)

while True:
    ret, frame = webcam.read()
    if not ret:
        break
    cv.imshow('WebCam', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv.destroyAllWindows()

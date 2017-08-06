import cv2
import numpy as np
from bokeh.colors import darkred


sensitivity = 15
hsvColorH = 25

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # HSV: Hue, Saturation, Value
    # You can find the HSV value by convert BGR to HSV
    # For example: hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
    # darkRed = np.uint8([[[12,22,121]]])
    # darkRed = cv2.cvtColor(darkRed, cv2.COLOR_BGR2HSV)
    
    lowerRed = np.array([hsvColorH-sensitivity,0,0])
    upperRed = np.array([hsvColorH+sensitivity,255,255])


    
    
    mask = cv2.inRange(hsv, lowerRed, upperRed)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    grayScaled = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    gaus = cv2.adaptiveThreshold(grayScaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
    retval3, otsu = cv2.threshold(grayScaled, 70, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    
    
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('result', res)
    cv2.imshow('gauss', gaus)
    cv2.imshow('otsu', otsu)
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
cap.release()

    

import cv2
import numpy as np
from bokeh.colors import darkred


sensitivity = 10
hsvColorH = 30

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
    
    # Try to remove noise
    
    kernel = np.ones((15,15), np.float32)/225
    smoothed = cv2.filter2D(res, -1, kernel)
    
    blur = cv2.GaussianBlur(res, (15,15), 0)
    
    median = cv2.medianBlur(res, 15)
    
    bilateral = cv2.bilateralFilter(res, 15, 75,75)
    
    kernel = np.ones((5,5), np.uint8)
    erosion = cv2.erode(mask, kernel, iterations= 1)
    dilation = cv2.dilate(mask, kernel, iterations= 1)
    
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
#     cv2.imshow('result', res)
#     cv2.imshow('gauss', gaus)
#     cv2.imshow('otsu', otsu)
#     cv2.imshow('smoothed', smoothed)
#     cv2.imshow('blur', blur)
#     cv2.imshow('median', median)
#     cv2.imshow('bilateral', bilateral)
    cv2.imshow('erosion', erosion)
    cv2.imshow('dilation', dilation)
    cv2.imshow('opening', opening)
    cv2.imshow('closing', closing)
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
cap.release()

    

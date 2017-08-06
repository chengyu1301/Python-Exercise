import numpy as np
import cv2

FILENAME = 'car.jpg'

img = cv2.imread(FILENAME)
retval, threshold = cv2.threshold(img, 70, 255, cv2.THRESH_BINARY)
grayScaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(grayScaled, 70, 255, cv2.THRESH_BINARY)
gaus = cv2.adaptiveThreshold(grayScaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
retval3, otsu = cv2.threshold(grayScaled, 70, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)


cv2.imshow('origin', img)
cv2.imshow('threshold', threshold)
cv2.imshow('grayScaled', grayScaled)
cv2.imshow('threshold2', threshold2)
cv2.imshow('gaus', gaus)
cv2.imshow('otsu', otsu)

cv2.imwrite(FILENAME+'GrayScaled.jpg', grayScaled)
cv2.imwrite(FILENAME+'Threshold.jpg', threshold)
cv2.imwrite(FILENAME+'Threshold2.jpg', threshold2)
cv2.imwrite(FILENAME+'Gauss.jpg', gaus)
cv2.imwrite(FILENAME+'Otsu.jpg', otsu)

cv2.waitKey(0)
cv2.destroyAllWindows()
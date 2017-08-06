import numpy as np
import cv2

img1 = cv2.imread('kana.png')
img2 = cv2.imread('kana3.png')
img3 = cv2.imread('kumamon.jpg')


add = img1//2 + img2//2
cv2.imshow('add', add)
cv2.waitKey(0)

add = cv2.add(img1, img2)
cv2.imshow('add', add)
cv2.waitKey(0)

add = cv2.addWeighted(img1, 0.8, img2, 0.2, 0)
cv2.imshow('add', add)
cv2.waitKey(0)

rows, cols, channels = img2.shape
roi = img3[0+300:rows+300, 0+300:cols+300]

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 100, 255, cv2.THRESH_BINARY_INV)

cv2.imshow('mask', mask)
cv2.waitKey(0)

maskInv = cv2.bitwise_not(mask)
img3Bg = cv2.bitwise_and(roi, roi, mask=mask)
cv2.imshow('img3Bg', img3Bg)
cv2.waitKey(0)

img2Fg = cv2.bitwise_and(img2, img2, mask=maskInv)
cv2.imshow('img2Fg', img2Fg)
cv2.waitKey(0)

dst = cv2.add(img3Bg, img2Fg)
img3[0+300:rows+300, 0+300:cols+300] = dst
cv2.imshow('final', img3)
cv2.waitKey(0)

cv2.imwrite('kumamonKana.jpg', img3)

cv2.destroyAllWindows()


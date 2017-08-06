import numpy as np
import cv2

img = cv2.imread('kumamon.jpg', cv2.IMREAD_COLOR)

img[55,55] = [255,255,255]
px = img[55,55]

regionOfImage = img[100:150, 100:150]
print(regionOfImage)

img[100:150, 100:150] = [0,0,255]
kumamon = img[100:500, 100:500]
img[0:400, 0:400] = kumamon

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
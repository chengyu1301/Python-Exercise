import cv2
import numpy as np
import matplotlib.pyplot as plt

#=====To read image=====#
img = cv2.imread('kumamon.jpg', cv2.IMREAD_GRAYSCALE)

#=====To show image by cv2=====#
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#=====To write file=====#
cv2.imwrite('kumamonmon.jpg', img)

#=====To show image by matplotlib=====#
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.plot([50,100], [80,100], 'c', linewidth=5) #To plot a line on img
plt.show()

#=====Create a new windows and show img=====#
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()



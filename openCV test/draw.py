import cv2
import numpy as np
import matplotlib as plt

img = cv2.imread('kumamon.jpg', cv2.IMREAD_COLOR)

cv2.line(img, (0,0), (150,150), (255,255,255), 15)
cv2.rectangle(img, (15,25), (200, 150), (255,0,0), 5)
cv2.circle(img, (100,63), 50, (0,255,0), -1)

points = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
#points = points.reshape((-1,1,2))
cv2.polylines(img, [points], True, (0,255,255), 3)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV tutorial', (250,60), font, 1, (20,20,255), 2, cv2.LINE_AA)


cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('kumamonDraw.jpg', img)
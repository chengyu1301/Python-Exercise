import cv2
import numpy as np

imgBGR = cv2.imread('back.jpg')
imgGray = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2GRAY)

template = cv2.imread('template.jpg', 0)
w, h= template.shape[::-1]
result = cv2.matchTemplate(imgGray, template, cv2.TM_CCOEFF_NORMED)

threshold = 0.5
location = np.where(result >= threshold)

for pt in zip(*location[::-1]):
    cv2.rectangle(imgBGR, pt, (pt[0]+w, pt[1]+h), (0,255,255), 2)
    
template2 = cv2.imread('template2.jpg', 0)
w, h= template2.shape[::-1]
result = cv2.matchTemplate(imgGray, template2, cv2.TM_CCOEFF_NORMED)    
for pt in zip(*location[::-1]):
    cv2.rectangle(imgBGR, pt, (pt[0]+w, pt[1]+h), (0,255,255), 2)
    
cv2.imshow('detected', imgBGR)
cv2.imwrite('detected.jpg', imgBGR)    
cv2.waitKey(0)
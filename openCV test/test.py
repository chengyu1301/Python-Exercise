# import cv2
# import numpy as np
import cv2
import numpy as np


# img_rgb = cv2.imread('back.jpg')
# img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
imgBGR = cv2.imread('back.jpg')
imgGray = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2GRAY)


# template = cv2.imread('template.jpg',0)
template = cv2.imread('template.jpg', 0)
# w, h = template.shape[::-1]
# res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)

# threshold = 0.8
# loc = np.where( res >= threshold)
# for pt in zip(*loc[::-1]):
    # cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)

# cv2.imshow('Detected',img_rgb)
# cv2.waitKey(0)










cv2.imshow('origin', imgBGR)
cv2.imshow('gray', imgGray)

w, h = template.shape[::-1]
print(w, h)

result = cv2.matchTemplate(imgGray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
location = np.where(result >= threshold)

for pt in zip(*location[::-1]):
    cv2.rectangle(imgBGR, pt, (pt[0]+w, pt[1]+h), (0,255,255), 2)
    
    cv2.imshow('detected', imgBGR)



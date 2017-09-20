import numpy as np

# only for osx or windows
# from PIL import ImageGrab

# use this for ubuntu
# sudo apt-get install python-pil
# sudo pip3 install pyscreenshot

import pyscreenshot as ImageGrab
import cv2
import time


def processImg(originImg):
    processedImg = cv2.cvtColor(originImg, cv2.COLOR_BGR2GRAY)
    processedImg = cv2.Canny(processedImg, threshold1=200, threshold2=300)  # edge detection
    return processedImg

def screen_record(): 
    last_time = time.time()
    while(True):
        # 800x600 windowed mode for GTA 5, at the top left position of your main screen.
        # 40 px accounts for title bar. 
        printscreen =  np.array(ImageGrab.grab(bbox=(0,40,800,640))) # 40 for title bar
        newScreen = processImg(printscreen)
        # print('loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        cv2.imshow('window',newScreen)
        cv2.imshow('window2',cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(20) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

screen_record()

#-*- coding: utf-8 -*-

# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html
# http://monkeycoding.com/?page_id=12



import cv2

#=====Read, show, and write image=====#

cv2.imread(string fileName, int flags)

    # flags = [cv2.IMREAD_COLOR: 1,
             cv2.IMREAD_GRAYSCALE: 0, 
             cv2.IMREAD_UNCHANGED: -1]

cv2.namedWindow(string frameName, int flags)    # Create a new window

    # flags = [cv2.WINDOW_AUTOSIZE,
             cv2.WINDOW_NORMAL]
   
cv2.imshow(string frameName, mat frame)

cv2.imwrite(string frameName, mat frame)

cv2.waitKey(milisec)

cv2.destroyAllWindows()


#=====Capture Video from Camera=====#


cv2.VideoCapture(arg) # Create a video object

    # arg = [device id | filename]
    
ret, frame = cv2.cap.read()  # returns a bool (True/False)
                             # use cap.isOpened() to check if open
                             # cap.open()

cap.get(propId) # access some of the features of this video
                # propId is a number from 0 to 18
                # cap.set(propId, value) to set attributes

fourcc = cv2.VideoWriter_fourcc(*'XVID') # 4-byte code used to specify the video codec
fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
                                        
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480)) # create a VideoWriter object

    # args: filename, fourcc, frame rate, frame size

cv2.imwrite(filename) # write file


#=====Drawing=====#

#     img : The image where you want to draw the shapes
#     color : Color of the shape. for BGR, pass it as a tuple, eg: (255,0,0) for blue. For grayscale, just pass the scalar value.
#     thickness : Thickness of the line or circle etc. If -1 is passed for closed figures like circles, it will fill the shape. default thickness = 1
#     lineType : Type of line, whether 8-connected, anti-aliased line etc. By default, it is 8-connected. cv2.LINE_AA gives anti-aliased line which looks great for curves.


img = np.zeros((512,512,3), np.uint8) # create image

img = cv2.line(img,(0,0),(511,511),(255,0,0),5) # draw line

    # args: img, start pt, end pt, color, thickness
    
img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3) # draw rectangle

    # args: img, top-left pt, bottom-right pt, color, thickness
    
img = cv2.circle(img,(447,63), 63, (0,0,255), -1) # draw circle

    # args: img, center pt, radius, color, thickness
    
img = cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1) # draw eclipse

    # args: img, center pt, axes lengths(x and y), angle, startAngle, endAngle, color, thickness
    
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],True,(0,255,255)) # draw Polygon
    
    # args: img, poly pts, closeShape, color
    
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA # Add text
            
    # Text data that you want to write
    # Position coordinates of where you want put it (i.e. bottom-left corner where data starts).
    # Font type (Check cv2.putText() docs for supported fonts)
    # Font Scale (specifies the size of font)
    # regular things like color, thickness, lineType etc. For better look, lineType = cv2.LINE_AA is recommended.
    

#=====Convert=====#
cv2.cvtColor(input_image, flag)
    # cv2.COLOR_BGR2GRAY, cv2.COLOR_BGR2HSV
    
    # For HSV, Hue range is [0,179], Saturation range is [0,255] and Value range is [0,255]. Different softwares use different scales. So if you are comparing OpenCV values with them, you need to normalize these ranges.
    
    # Now you take [H-10, 100,100] and [H+10, 255, 255] as lower bound and upper bound respectively. Apart from this method, you can use any image editing tools like GIMP or any online converters to find these values, but don’t forget to adjust the HSV ranges.
    

lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255]) # define range of blue color in HSV

mask = cv2.inRange(hsv, lower_blue, upper_blue) # Threshold the HSV image to get only blue colors


#=====Image Thresholding=====#



ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    
    # First argument is the source image, which should be a grayscale image. 
    # Second argument is the threshold value which is used to classify the pixel values. 
    # Third argument is the maxVal which represents the value to be given if pixel value is more than (sometimes less than) the threshold value.
    
    
    # Two outputs are obtained. 
    # First one is a retval which will be explained later. 
    # Second output is our thresholded image.
    
    # Threshold Types:
        # cv2.THRESH_BINARY
        # cv2.THRESH_BINARY_INV
        # cv2.THRESH_TRUNC
        # cv2.THRESH_TOZERO
        # cv2.THRESH_TOZERO_INV
        
#=====ADAPTIVE THRESHOLD=====#
        
ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
    
    # 255: max value: 0 <- threshold -> 255
    
    # cv2.ADAPTIVE_THRESH_MEAN_C : threshold value is the mean of neighbourhood area.
    
    # cv2.ADAPTIVE_THRESH_GAUSSIAN_C : threshold value is the weighted sum of neighbourhood values where weights are a gaussian window.
    
    # Block Size - It decides the size of neighbourhood area. (odd)
    
    # C - It is just a constant which is subtracted from the mean or weighted mean calculated.
    
    
#=====Otsu’s Binarization=====#    

    # global thresholding
    ret1,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

    # Otsu's thresholding
    ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    # Otsu's thresholding after Gaussian filtering
    blur = cv2.GaussianBlur(img,(5,5),0)
    ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    

#=====Smoothing Images=====#

kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)

    # src：當ksize為3或5時，輸入可以為多通道的CV_8U、CV_16U或CV_32F，在更大的模板時，只能操作CV_8U的型態。
    # dst：輸出圖會和輸入圖尺寸、型態相同。
    # ksize：模板大小，必須為大於1的正奇數，像3、5、7……


blur = cv2.blur(img,(5,5)) # average blur

blur = cv2.GaussianBlur(img,(5,5),0) # Gaussian Blur

median = cv2.medianBlur(img,5) # median Blur

blur = cv2.bilateralFilter(img,9,75,75) # Bilateral Filtering 雙邊濾波


#=====Template Matching=====#
res = cv2.matchTemplate(img,template,method)

# methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
      
      
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED) # to find location
threshold = 0.8
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
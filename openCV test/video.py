import cv2
import numpy as np

# open the camera 0 on the computer
cap = cv2.VideoCapture(0)

# select encoding of saving file
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# open the saving file: filename, encoding, frame per second, frame size
outputFile = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    outputFile.write(frame)
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()
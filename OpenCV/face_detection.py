import cv2
import numpy as np
print(cv2.__version__)

dispW=1280
dispH=720
flip=2
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

cam=cv2.VideoCapture(camSet)




face=cv2.CascadeClassifier('/home/aman/pypro/haar/haarcascade_frontalface_default.xml')
eye=cv2.CascadeClassifier('/home/aman/pypro/haar/haarcascade_eye.xml')

while True:
    ret, frame=cam.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face1=face.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in face1:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        roi=gray[y:y+h,x:x+w]
        roic=frame[y:y+h,x:x+w]
        eyes=eye.detectMultiScale(roi)
        for (x1,y1,x2,y2) in eyes:
            cv2.rectangle(roic,(x1,y1),(x1+x2,y1+y2),(255,0,0),2)
    
    cv2.imshow('piCam',frame)
    cv2.moveWindow('piCam',0,0)
    
   
    if cv2.waitKey(1)==ord('q'):#keep waitKey(50) if recording in 720p and higher
        break

cam.release()
cv2.destroyAllWindows() 
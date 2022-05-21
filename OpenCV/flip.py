import cv2
import numpy as np
print(cv2.__version__)

dispW=640
dispH=480
flip=0
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

cam=cv2.VideoCapture(camSet)







while True:
    ret, frame=cam.read()

    for i in range(0,240,1):
       
            temp=frame[i]
            frame[479-i]=frame[i]
            frame[479-i]=temp
    
    cv2.imshow('piCam',frame)
    cv2.moveWindow('piCam',0,0)
    
   
    if cv2.waitKey(1)==ord('q'):#keep waitKey(50) if recording in 720p and higher
        break

cam.release()
cv2.destroyAllWindows() 
import cv2
import numpy as np
print(cv2.__version__)
blank=np.zeros([480,640,1],np.uint8)
dispW=640
dispH=480
flip=0
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

cam=cv2.VideoCapture(camSet)


 


while True:
    ret, frame=cam.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    bluec,greenc,redc=cv2.split(frame)
    #redc=cv2.merge((blank,blank,redc))
    #greenc=cv2.merge((blank,greenc,blank))
    #bluec=cv2.merge((bluec,blank,blank))
    _,greenc=cv2.threshold(greenc,90,255,cv2.THRESH_BINARY)
    greenc=cv2.bitwise_and(frame,frame,mask=greenc)
    #g[:]=g[:]*.1
    cv2.imshow('piCam',frame)
    cv2.moveWindow('piCam',0,0)
    cv2.imshow('Blue',bluec)
    cv2.moveWindow('Blue',700,0)
    cv2.imshow('Green',greenc)
    cv2.moveWindow('Green',0,500)
    cv2.imshow('Red',redc)
    cv2.moveWindow('Red',700,500)
    
   
    if cv2.waitKey(1)==ord('q'):#keep waitKey(50) if recording in 720p and higher
        break

cam.release()
cv2.destroyAllWindows() 
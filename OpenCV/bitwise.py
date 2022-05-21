import cv2
import numpy as np
print(cv2.__version__)
img1=np.zeros((480,640,1),np.uint8)
img2=np.zeros((480,640,1),np.uint8)
dispW=640
dispH=480
flip=0
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
img1[0:480,0:320]=[255]
img2[190:290,270:370]=[255]
bitAnd=cv2.bitwise_and(img1,img2)
bitOr=cv2.bitwise_or(img1,img2) 
bitXor=cv2.bitwise_xor(img1,img2)
cam=cv2.VideoCapture(camSet)
cv2.namedWindow('piCam')
while True:
    ret, frame=cam.read()
   
    frame=cv2.bitwise_and(frame,frame,mask=bitXor)
    cv2.imshow('plain',img1)
    cv2.moveWindow('plain',0,500)
    cv2.imshow('plain2',img2)
    cv2.moveWindow('plain2',700,0)
    cv2.imshow('plainor',bitOr)
    cv2.moveWindow('plainaor',1400,0) 
    cv2.imshow('plainxor',bitXor)
    cv2.moveWindow('plainaxor',1400,500) 
    cv2.imshow('plainand',bitAnd)
    cv2.moveWindow('plainand',700,500)
    
    cv2.imshow('piCam',frame)
    cv2.moveWindow('piCam',0,0)
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
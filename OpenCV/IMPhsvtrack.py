import cv2
import numpy as np
print(cv2.__version__)
blank=np.zeros([480,640,1],np.uint8)
dispW=640
dispH=480
flip=0
def nothing(x):
    pass
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

cam=cv2.VideoCapture(camSet)


cv2.namedWindow('im')
cv2.moveWindow('im',1320,0)



cv2.createTrackbar('hueLow','im',50,179,nothing)
cv2.createTrackbar('hueHigh','im',100,179,nothing)
cv2.createTrackbar('hueLow1','im',50,179,nothing)
cv2.createTrackbar('hueHigh1','im',100,179,nothing)
cv2.createTrackbar('satLow','im',100,255,nothing)
cv2.createTrackbar('satHigh','im',255,255,nothing)
cv2.createTrackbar('valLow','im',100,255,nothing)
cv2.createTrackbar('valHigh','im',255,255,nothing)





while True:
    ret, logo=cam.read()
    
    
    
   
    #logo=cv2.imread('OpenCV/smarties.png')
    logoh=cv2.cvtColor(logo,cv2.COLOR_BGR2HSV)
    
    hueLow=cv2.getTrackbarPos('hueLow','im')
    hueHigh=cv2.getTrackbarPos('hueHigh','im')
    hueLow1=cv2.getTrackbarPos('hueLow1','im')
    hueHigh1=cv2.getTrackbarPos('hueHigh1','im')
    satHigh=cv2.getTrackbarPos('satHigh','im')
    satLow=cv2.getTrackbarPos('satLow','im')
    valLow=cv2.getTrackbarPos('valLow','im')
    valHigh=cv2.getTrackbarPos('valHigh','im')

    l_b=np.array([hueLow,satLow,valLow])
    u_b=np.array([hueHigh,satHigh,valHigh])

    l_b1=np.array([hueLow1,satLow,valLow])
    u_b1=np.array([hueHigh1,satHigh,valHigh])

    FGMask1=cv2.inRange(logoh,l_b1,u_b1)
    

    FGMask=cv2.inRange(logoh,l_b,u_b)
    final1=cv2.add(FGMask,FGMask1)
    FG=cv2.bitwise_and(logo,logo,mask=final1)
   

    BGMask=cv2.bitwise_not(final1)
    BG=cv2.cvtColor(BGMask,cv2.COLOR_GRAY2BGR)
    final=cv2.add(FG,BG)
    

    cv2.imshow('im1',logo)
    cv2.moveWindow('im1',0,0)
    cv2.imshow('Blue',FGMask)
    cv2.moveWindow('Blue',700,0)
    cv2.imshow('Green',FG)
    cv2.moveWindow('Green',0,500)
    #cv2.imshow('piCam',frame)
    #cv2.moveWindow('piCam',0,0)
    cv2.imshow('Red',final)
    cv2.moveWindow('Red',700,500)
    
   
    if cv2.waitKey(1)==ord('q'):#keep waitKey(50) if recording in 720p and higher
        break

cam.release()
cv2.destroyAllWindows() 
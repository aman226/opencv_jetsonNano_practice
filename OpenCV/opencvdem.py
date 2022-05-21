import cv2
print(cv2.__version__)

dispW=640
dispH=480
flip=2
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
#for web cam   cam=cv2.VideoCapture(0)
#              cam.set(cv2.CAP_PROP_FRAME_WIDTH,widthVal)
#              cam.set(cv2.CAP_PROP_FRAME_HEIGHT,heighVal)
cam=cv2.VideoCapture(camSet)
while True:
    ret, frame=cam.read()
    
    cv2.imshow('piCam',frame)
    cv2.moveWindow('piCam',0,0) 
    
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('grayVideo',gray)
    cv2.moveWindow('grayVideo',0,500)#for moving
    frameSmall=cv2.resize(gray,(320,240))#for resizing
    
    cv2.imshow('smallVideo',frameSmall)
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows() 
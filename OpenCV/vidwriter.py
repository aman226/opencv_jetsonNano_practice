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
#cam=cv2.VideoCapture("filepath") if you want to capture from video file
fourcc = cv2.VideoWriter_fourcc(*'XVID')
outVid= cv2.VideoWriter('output.avi',fourcc, 21.0, (640,480))
while True:
    ret, frame=cam.read()
    if(ret==False):
        print("openCV can't read a frame (perhaps stream EOF?)... exiting now...")
        break
    
    cv2.imshow('piCam',frame)
    cv2.moveWindow('piCam',0,0) 
    
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('grayVideo',gray)
    cv2.moveWindow('grayVideo',0,500)#for moving
    outVid.write(frame)
    frameSmall=cv2.resize(gray,(320,240))#for resizing
    
    cv2.imshow('smallVideo',frameSmall)
    if cv2.waitKey(1)==ord('q'):#keep waitKey(50) if recording in 720p and higher
        break

cam.release()
outVid.release()
cv2.destroyAllWindows() 
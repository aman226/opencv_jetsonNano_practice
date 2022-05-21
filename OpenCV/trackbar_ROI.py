import cv2
print(cv2.__version__)
def nothing(x):
    pass
dispW=640
dispH=480
flip=0
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

cam=cv2.VideoCapture(camSet)
cv2.namedWindow('piCam')
cv2.createTrackbar('xVal','piCam',25,640,nothing)
cv2.createTrackbar('yVal','piCam',25,480,nothing)
cv2.createTrackbar('width','piCam',25,640,nothing)
cv2.createTrackbar('height','piCam',25,480,nothing)
while True:
    ret, frame=cam.read()
    xVal=cv2.getTrackbarPos('xVal','piCam')
    yVal=cv2.getTrackbarPos('yVal','piCam')
    width=cv2.getTrackbarPos('width','piCam')
    height=cv2.getTrackbarPos('height','piCam')
    #roi=frame[50:250,200:400].copy()
    #roiGray=cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
    #frame[50:250,200:400]=[255,255,255]
    #cv2.imshow('gray',roiGray)
    #cv2.moveWindow('gray',705,705)
    roi=frame[yVal:yVal+height,xVal:xVal+width].copy() 
    roiGray=cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
    roiGray=cv2.cvtColor(roiGray,cv2.COLOR_GRAY2BGR)
    frame[yVal:yVal+height,xVal:xVal+width]=roiGray
    #frame=cv2.rectangle(frame,(xVal,yVal),(xVal+width,yVal+height),(255,0,150),7)
    cv2.imshow('piCam',frame)
    cv2.imshow('ROI',roi)
    cv2.imshow('gray',roiGray)
    cv2.moveWindow('gray',705,705)
    cv2.moveWindow('piCam',0,0)
    cv2.moveWindow('ROI',800,0) 
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
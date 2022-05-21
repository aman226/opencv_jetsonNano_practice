import cv2
import numpy as np
print(cv2.__version__)
flag=0

#PROGRAMME DOESNT WORK FOR OTHER DRAGGING DIRECTION EXCEPT LEFT TO RIGHT
def click(event,x,y,flags,params):
    global x1,x2,y1,y2,flag
    if event==cv2.EVENT_LBUTTONDOWN:
        y1=y
        x1=x
        flag=0
    if event==cv2.EVENT_LBUTTONUP:
        y2=y
        x2=x
        flag=1


dispW=640
dispH=480
flip=0
cv2.namedWindow('piCam')
cv2.setMouseCallback('piCam',click)
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

cam=cv2.VideoCapture(camSet)


while True:
    ret, frame=cam.read()

    if flag is 1:
        roi=frame[y1:y2,x1:x2]
        
        
        
        roi=cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
        roi=cv2.cvtColor(roi,cv2.COLOR_GRAY2BGR)
        frame[y1:y2,x1:x2]=roi
        frame=cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,255),1)
    cv2.imshow('piCam',frame)
    cv2.moveWindow('piCam',0,0)
    keyEvent=cv2.waitKey(1)
    
    if keyEvent==ord('q'):#keep waitKey(50) if recording in 720p and higher
        break
    if keyEvent==ord('c'):
        flag=0
cam.release()
cv2.destroyAllWindows() 
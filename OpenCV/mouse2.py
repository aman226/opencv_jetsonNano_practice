import cv2
import numpy as np
print(cv2.__version__)

coord=[]
img=np.zeros((250,250,3),np.uint8)

def click(event,x,y,flags,params):
    global pnt
    global evt
    if event==cv2.EVENT_LBUTTONDOWN:
        print('MOUSE EVENT WAS: ',event)
        pnt=(x,y)
        coord.append(pnt)
        print(coord)
        evt=event
    if event==cv2.EVENT_RBUTTONDOWN:
        print(x,y)
        blue=frame[y,x,0]
        green=frame[y,x,1]
        red=frame[y,x,2]
        print(blue,green,red)
        colorString=str(blue)+','+str(green)+','+str(red)
        img[:]=[blue,green,red]
        fnt=cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(img,colorString,(10,25),fnt,1,(255-int(blue),255-int(green),255-int(red)),2)
        cv2.imshow('myColor',img)


dispW=640
dispH=480
flip=0
cv2.namedWindow('piCam')
cv2.setMouseCallback('piCam',click)
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

cam=cv2.VideoCapture(camSet)


while True:
    ret, frame=cam.read()
    for pnts in coord:
        cv2.circle(frame,pnts,5,(0,0,255),-1)
        
    cv2.imshow('piCam',frame)
    cv2.moveWindow('piCam',0,0)
    keyEvent=cv2.waitKey(1)
    if keyEvent==ord('q'):#keep waitKey(50) if recording in 720p and higher
        break
    if keyEvent==ord('c'):#keep waitKey(50) if recording in 720p and higher
        coord=[]

cam.release()
cv2.destroyAllWindows() 
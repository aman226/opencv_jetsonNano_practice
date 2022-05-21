import cv2
print(cv2.__version__)
evt=-1
def click(event,x,y,flags,params):
    global pnt
    global evt
    if event==cv2.EVENT_LBUTTONDOWN:
        print('MOUSE EVENT WAS: ',event)
        pnt=(x,y)
        evt=event

dispW=640
dispH=480
flip=0
cv2.namedWindow('piCam')
cv2.setMouseCallback('piCam',click)
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

cam=cv2.VideoCapture(camSet)


while True:
    ret, frame=cam.read()
    if evt==1:
        cv2.circle(frame,pnt,5,(0,0,255),-1)
        fnt=cv2.FONT_HERSHEY_DUPLEX
        myStr=str(pnt)
        frame=cv2.putText(frame,myStr,pnt,fnt,1,(255,255,0),2)

    cv2.imshow('piCam',frame)
    cv2.moveWindow('piCam',0,0)
    if cv2.waitKey(1)==ord('q'):#keep waitKey(50) if recording in 720p and higher
        break

cam.release()
cv2.destroyAllWindows() 
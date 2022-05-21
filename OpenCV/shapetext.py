import cv2
print(cv2.__version__)

dispW=640
dispH=480
flip=2
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

cam=cv2.VideoCapture(camSet)
while True:
    ret, frame=cam.read()
    if(ret==False):
        print("openCV can't read a frame (perhaps stream EOF?)... exiting now...")
        break
    frame=cv2.rectangle(frame,(340,100),(590,400),(0,256,0),7)
    frame=cv2.circle(frame,(320,240),100,(255,255,0),6)#negative width for solid fill
    fnt=cv2.FONT_HERSHEY_DUPLEX
    frame=cv2.putText(frame,'HEHE',(280,240),fnt,2,(255,255,0),2)
    frame=cv2.line(frame,(10,10),(630,470),(255,255,0),3)
    frame=cv2.arrowedLine(frame,(10,470),(630,10),(255,0,150),3)
    cv2.imshow('piCam',frame)
    cv2.moveWindow('piCam',0,0) 
    if cv2.waitKey(1)==ord('q'):#keep waitKey(50) if recording in 720p and higher
        break

cam.release()
cv2.destroyAllWindows() 
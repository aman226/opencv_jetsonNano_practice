import cv2
print(cv2.__version__)

dispW=640
dispH=480
flip=0
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

cam=cv2.VideoCapture(camSet)
bw=int(.15*dispW)
bh=int(.25*dispH)
posx=10
posy=270
dx=2
dy=2

while True:
    ret, frame=cam.read()

    

    frame=cv2.rectangle(frame,(posx,posy),(posx+bw,posy+bh),(255,150,0),2)
    roi=frame[posy:posy+bh,posx:posx+bw].copy() 
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame=cv2.cvtColor(frame,cv2.COLOR_GRAY2BGR)
    frame[posy:posy+bh,posx:posx+bw]=roi
    cv2.imshow('piCam',frame)
    cv2.moveWindow('piCam',0,0)
    posx=posx+dx
    posy=posy+dy
    if posx<=0 or posx+bw>=dispW:
        dx=dx*(-1)
    if posy<=0 or posy+bh>=dispH:
        dy=dy*(-1)
   
    if cv2.waitKey(1)==ord('q'):#keep waitKey(50) if recording in 720p and higher
        break

cam.release()
cv2.destroyAllWindows() 
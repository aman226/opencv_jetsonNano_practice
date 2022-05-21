import cv2
print(cv2.__version__)

dispW=640
dispH=480
flip=0
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

cam=cv2.VideoCapture(camSet)
bw=int(.25*dispW)
bh=int(.25*dispH)
posx=10
posy=270
dx=2
dy=2


Logo=cv2.imread('/home/aman/pypro/OpenCV/pl.jpg')
Logo=cv2.resize(Logo,(bw,bh))
LogoGray=cv2.cvtColor(Logo,cv2.COLOR_BGR2GRAY)
_,BGMask=cv2.threshold(LogoGray,225,255,cv2.THRESH_BINARY)
FGMask=cv2.bitwise_not(BGMask)
FG=cv2.bitwise_and(Logo,Logo,mask=FGMask)
cv2.imshow('mas',FG)
cv2.moveWindow('mas',700,0)




while True:
    ret, frame=cam.read()

    
    frame2=frame[posy:posy+bh,posx:posx+bw].copy()
    
    FIG=cv2.bitwise_and(frame2,frame2,mask=BGMask)
    FIN=cv2.add(FIG,FG)
    frame[posy:posy+bh,posx:posx+bw]=FIN
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
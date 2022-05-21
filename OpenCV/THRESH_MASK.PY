import cv2

print(cv2.__version__)
dispW=320
dispH=240
flip=0
def nothing(X):
    pass
cv2.namedWindow('ffin')
cv2.createTrackbar('Blendval','ffin',50,100,nothing)
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cvLogo=cv2.imread('/home/aman/pypro/OpenCV/cv.jpg')
cvLogo=cv2.resize(cvLogo,(320,240))
cvLogoGray=cv2.cvtColor(cvLogo,cv2.COLOR_BGR2GRAY)
cv2.imshow('OPEN',cvLogoGray)
cv2.moveWindow('OPEN',0,350)

_,BGMask=cv2.threshold(cvLogoGray,225,255,cv2.THRESH_BINARY)
cv2.imshow('mas',BGMask)
cv2.moveWindow('mas',350,0)

FGMask=cv2.bitwise_not(BGMask)

cv2.imshow('fmas',FGMask)
cv2.moveWindow('fmas',380,300)

FG=cv2.bitwise_and(cvLogo,cvLogo,mask=FGMask)

cv2.imshow('fmask',FG)
cv2.moveWindow('fmask',380,350)


cam=cv2.VideoCapture(camSet)
cv2.namedWindow('piCam')
while True:
    ret, frame=cam.read()
    BG=cv2.bitwise_and(frame,frame,mask=BGMask)
    fin=cv2.add(BG,FG)
    x1=cv2.getTrackbarPos('Blendval','ffin')
    blend=cv2.addWeighted(frame,x1/100,cvLogo,(100-x1)/100,0)
    FG2=cv2.bitwise_and(blend,blend,mask=FGMask)
    FINAL=cv2.add(FG2,BG)
    cv2.imshow('fg2',FG2)
    cv2.moveWindow('fg2',1324,100)
    cv2.imshow('piCam',frame)  
    cv2.moveWindow('piCam',0,0)
    cv2.imshow('fin',fin)  
    cv2.moveWindow('fin',1017,100)
    cv2.imshow('ffin',FINAL)  
    cv2.moveWindow('ffin',1324,350)
    cv2.imshow('mask',BG)  
    cv2.moveWindow('mask',660,0)
    cv2.imshow('mask1',blend)  
    cv2.moveWindow('mask2',660,300)
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
import cv2
print(cv2.__version__)

dispW=640
dispH=480
flip=0
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

cam=cv2.VideoCapture(camSet)
i=1
j=1
flagi=0
flagj=0
while True:
    ret, frame=cam.read()
    if(ret==False):
        print("openCV can't read a frame (perhaps stream EOF?)... exiting now...")
        break
    if(i==0):
        flagi=0
    elif(i+100==640):
        flagi=1   
    if(j==0):
        flagj=0
    elif(j+100==480):
        flagj=1 
    

    frame=cv2.rectangle(frame,(i,j),(i+100,j+100),(255,150,0),-7)
    cv2.imshow('piCam',frame)
    cv2.moveWindow('piCam',0,0)
    
    if(flagi==0):
        i=i+1
    elif(flagi==1):
        i=i-1
    if(flagj==0):
        j=j+1
    elif(flagj==1):
        j=j-1

    if cv2.waitKey(1)==ord('q'):#keep waitKey(50) if recording in 720p and higher
        break

cam.release()
cv2.destroyAllWindows() 
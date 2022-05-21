import face_recognition as fr
import cv2
import pickle
import time
print(cv2.__version__)
fpsReport=0
scaleFactor=0.25
cv2.namedWindow('mywindow')
dispW=640
dispH=480
flip=0
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

cam=cv2.VideoCapture(camSet)

ENCODINGS=[]
NAMES=[]

with open('/home/aman/pypro/train.pkl','rb') as f:
    NAMES=pickle.load(f)
    ENCODINGS=pickle.load(f)    

font=cv2.FONT_HERSHEY_DUPLEX
timeStamp=time.time()
while True:
    ret, frame=cam.read()
    frameSmall=cv2.resize(frame,(0,0),fx=scaleFactor,fy=scaleFactor)
    frameRGB=cv2.cvtColor(frameSmall,cv2.COLOR_BGR2RGB)
    facePositions=fr.face_locations(frameRGB)
    allEncodings=fr.face_encodings(frameRGB,facePositions)
    for (top,right,bottom,left),face_encoding in zip(facePositions,allEncodings):
         name='Unknown Person'
         match=fr.compare_faces(ENCODINGS,face_encoding)
         if True in match:
             fm=match.index(True)
             name=NAMES[fm]
         top=int(top/scaleFactor)
         left=int(left/scaleFactor)
         right=int(right/scaleFactor)
         bottom=int(bottom/scaleFactor)

         cv2.rectangle(frame,(left,top),(right,bottom),(0,255,0),2)
         cv2.putText(frame,name,(left,top-6),font,.75,(0,255,255),1)
    dt=time.time()-timeStamp
    fps=1/dt
    fps=round(fps,1)
    fpsReport=0.95*fps + 0.05*fpsReport
    print('FPS IS:',fpsReport)
    timeStamp=time.time()
    cv2.imshow('mywindow',frame)
    cv2.moveWindow('mywindow',0,0)
    if cv2.waitKey(1)== ord('q'):
        break
cam.release()
cv2.destroyAllWindows()

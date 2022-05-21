import face_recognition as fr
import cv2
import os
print(cv2.__version__) 
ENCODINGS=[]
NAMES=[]
j=0
imageDir='/home/aman/pypro/faceRecognizer/demoImages/known'

for (root,dirs,files) in os.walk(imageDir):
    for file in files:
        path=os.path.join(root,file)
        name=os.path.splitext(file)[0]
        print(name)
        person=fr.load_image_file(path)
        encoding=fr.face_encodings(person)[0]
        ENCODINGS.append(encoding)
        NAMES.append(name)
print(NAMES)

font=cv2.FONT_HERSHEY_DUPLEX

imageDir='/home/aman/pypro/faceRecognizer/demoImages/unknown'

for (root,dirs,files) in os.walk(imageDir):
    for file in files:
        path=os.path.join(root,file)
        testImage=fr.load_image_file(path)
        facePositions=fr.face_locations(testImage)
        allEncodings=fr.face_encodings(testImage,facePositions)
        testImage=cv2.cvtColor(testImage,cv2.COLOR_RGB2BGR)

        for (top,right,bottom,left),face_encoding in zip(facePositions,allEncodings):
            name='Unknown Person'
            match=fr.compare_faces(ENCODINGS,face_encoding)
            if True in match:
                fm=match.index(True)
                name=NAMES[fm]
            cv2.rectangle(testImage,(left,top),(right,bottom),(0,255,0),2)
            cv2.putText(testImage,name,(left,top-6),font,.75,(0,255,255),1)

        cv2.imshow('mywindow',testImage)
        cv2.moveWindow('mywindow',0,0)
        if cv2.waitKey(0)== ord('q'):
            cv2.destroyAllWindows() 
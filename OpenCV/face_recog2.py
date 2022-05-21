import face_recognition as fr
import cv2
font=cv2.FONT_HERSHEY_DUPLEX
print(cv2.__version__)
imaged=fr.load_image_file('/home/aman/pypro/faceRecognizer/demoImages/known/Donald Trump.jpg')
imagedEn=fr.face_encodings(imaged)[0]
imagen=fr.load_image_file('/home/aman/pypro/faceRecognizer/demoImages/known/Nancy Pelosi.jpg')
imagenEn=fr.face_encodings(imagen)[0]

imagep=fr.load_image_file('/home/aman/pypro/faceRecognizer/demoImages/known/Mike Pence.jpg')
imagepEn=fr.face_encodings(imagep)[0]

Encodings=[imagedEn,imagenEn,imagepEn]
Names=['Donald Trump','Nancu Pelosi','Mike Pence']

testImage=fr.load_image_file('/home/aman/pypro/faceRecognizer/demoImages/unknown/u11.jpg')
facePositions=fr.face_locations(testImage)


allEncodings=fr.face_encodings(testImage, facePositions)

testImage=cv2.cvtColor(testImage,cv2.COLOR_RGB2BGR)

for (top,right,bottom,left), face_encoding in  zip(facePositions,allEncodings):
    name='Unknown Person'
    match=fr.compare_faces(Encodings,face_encoding)
    if True in match:
        fm=match.index(True)
        name=Names[fm]
    cv2.rectangle(testImage,(left,top),(right,bottom),(0,255,0),2)
    cv2.putText(testImage,name,(left,top-6),font,.75,(0,255,255),1)

cv2.imshow('mywindow',testImage)
cv2.moveWindow('mywindow',0,0)
if cv2.waitKey(0)== ord('q'):
    cv2.destroyAllWindows() 
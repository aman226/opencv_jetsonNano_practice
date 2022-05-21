import face_recognition as fr
import cv2
print(cv2.__version__)
image=fr.load_image_file('/home/aman/pypro/faceRecognizer/demoImages/unknown/u14.jpg')
image=cv2.resize(image,(640,480))
faceloc=fr.face_locations(image)
print(faceloc)
image=cv2.cvtColor(image,cv2.COLOR_RGB2BGR)

for (x1,y1,x2,y2) in faceloc:
    cv2.rectangle(image,(y1,x1),(y2,x2),(0,255,0),2)
cv2.imshow('Window',image)
cv2.moveWindow('Window',0,0)
if cv2.waitKey(0)== ord('q'):
    cv2.destroyAllWindows()
    
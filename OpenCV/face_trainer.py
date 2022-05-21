import face_recognition as fr
import os
import pickle
ENCODINGS=[]
NAMES=[]
j=0
imageDir='/home/aman/pypro/faceRecognizer/demoImages/known'

for (root,dirs,files) in os.walk(imageDir):
    for file in files:
        path=os.path.join(root,file)
        name=os.path.splitext(file)[0]
        person=fr.load_image_file(path)
        encoding=fr.face_encodings(person)[0]
        print(name,' Training Done')
        ENCODINGS.append(encoding)
        NAMES.append(name)
print(NAMES)

with open('train.pkl','wb') as f:
    pickle.dump(NAMES,f)
    pickle.dump(ENCODINGS,f)
ENCODINGS=[]
NAME=[]
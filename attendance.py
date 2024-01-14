import os
import cv2
import face_recognition
import pickle

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL' : "https://faceattendancerealtime-7f62a-default-rtdb.firebaseio.com/",
    'storageBucket' : "faceattendancerealtime-7f62a.appspot.com"
})

#Importing the student images in a list
folderPath = 'Images'
PathList = os.listdir(folderPath)
imgList = []
studentIDs = []
for path in PathList:
    imgList.append(cv2.imread(os.path.join(folderPath,path)))
    studentIDs.append(os.path.splitext(path)[0])

    fileName = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)

folderPathNew = 'ImagesResized'
PathListNew = os.listdir(folderPathNew)

for path in PathListNew:
    fileName = f'{folderPathNew}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)

print(len(imgList))
print(studentIDs)

def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList
    
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIDs = [encodeListKnown,studentIDs]
#print(encodeListKnown)

file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnownWithIDs,file)
file.close()
print("File saved")
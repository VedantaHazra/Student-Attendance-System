import os
import cv2

folderPath = 'Images'
PathList = os.listdir(folderPath)

for path in PathList:
    path1 = os.path.join(folderPath,path)
    img = cv2.imread(path1)
    img1 = cv2.resize(img, (216,216))
    cv2.imwrite(path, img1)
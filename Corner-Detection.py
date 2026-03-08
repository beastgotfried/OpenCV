import cv2
import numpy as np
import random

cap = cv2.VideoCapture(0)

while (True):
    ret, frame= cap.read()
    width = int(cap.get(3))
    height= int(cap.get(4))
    
    img = cv2.imread('Chessboard.jpg',)
    img = cv2.resize(img , (0,0) , fx= 0.75, fy=0.75)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    corners = cv2.goodFeaturesToTrack(gray,100,0.01,10)
    corners= corners.astype(int)
    
    
    for corner in corners:
        x,y = corner.ravel()
        cv2.circle(img,(x,y),20,(255,0,0),-1)
    
    for i in range(len(corners)):
        for j in range(i+1,len(corners)):
            corner1=tuple(corners[i][0])
            corner2=tuple(corners[j][0])
            color= tuple(map(lambda x:int (x), np.random.randint(0,255,size=3)))
            cv2.line(img,corner1,corner2,color,3)
    
    
    cv2.imshow('nigger', img)
    
    
    if cv2.waitKey(1)==ord('q'):
        break
    
    
cap.release()
cv2.destroyAllWindows()
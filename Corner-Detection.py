import cv2
import numpy as np
import random

cap = cv2.VideoCapture(0)

while (True):
    ret, frame= cap.read()
    width = int(cap.get(3))
    height= int(cap.get(4))
    
    img = cv2.imread('Chessboard.jpg',)
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    corners = cv2.goodFeaturesToTrack(gray,100,0.01,10)  #corner detection algorithm
    corners= corners.astype(int) #converting corners to int datavalues
    
    
    for corner in corners:
        x,y = corner.ravel() #convert 3d arrays into 2d by flattening them
        cv2.circle(img,(x,y),20,(255,0,0),-1)   #draw circle from x,y taking corners as center
    
    for i in range(len(corners)):  #traversing between corners
        for j in range(i+1,len(corners)):  #traversing between missed corners so that 2 corners dont collide
            corner1=tuple(corners[i][0])   #converting corners into tuple so that data can be easily taken from
            corner2=tuple(corners[j][0])
            color= tuple(map(lambda x:int (x), np.random.randint(0,255,size=3)))   #randomise values from 0,254 and apply  int values to all of them and then convert them into a tuple becuase thats what opencv accepts
            cv2.line(img,corner1,corner2,color,3)
    
    
    cv2.imshow('nigger', img)
    
    
    if cv2.waitKey(1)==ord('q'):
        break
    
    
cap.release()
cv2.destroyAllWindows()
import cv2
import random

img = cv2.imread('images\clouds.png', 1)

#changing colors and schemas in an image

for i in range(0,200):
    for j in range(img.shape[1]):
        img[i][j]=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]
    

#copying and pasting images and its parts

tag= img[100:300, 100:300]

img[50:250, 50:250]= tag

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows
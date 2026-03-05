import cv2
#this is the way you can make opencv read your image
#by default opencv reads an image in bgr
img = cv2.imread('images/drizzle.png', cv2.IMREAD_COLOR )#can load in grayscale/color/removed transparency(opacity)

#resizing an image
img= cv2.resize(img,(0,0), fx=1,fy=1) #this is resizing the image by %

#rotate an image
img =cv2.rotate(img, cv2.ROTATE_180)

# -1, cv2.IMREAD_COLOR #reads an image with transparency neglected
# 0, cv2.IMREAD_GRAYSCALE #reads an image in black and white
# 1, cv2.IMREAD_UNCHANGED #reads an image in the colors it is in including opacity

cv2.imshow('image',img)  #creates a new window to display the image
cv2.waitKey(0) #waits infinity seconds before closing the window
cv2.destroyAllWindows   #when key pressed all windows are destroyed


#saving changes from one image to another
cv2.imwrite('newimg1.png', img)

print(img.shape) #image is taken in and pixels are grouped with each other through a nump array
#height, weidth,channel is how the order is 


print(img[100][45])

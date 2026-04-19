import cv2 

img = cv2.imread('Chessboard.jpg', cv2.IMREAD_GRAYSCALE) #reading the image in grayscale since edge detection algorithms only work that way

sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0 ,ksize=5) #implementing sobel edge matching for x axis
sobely= cv2.Sobel(img, cv2.CV_64F, 0,1, ksize= 5) #implementing sobel edge matching for y axis
 
sobel_magnitude= cv2.magnitude(sobelx,sobely) #finding magnitude and computing gradient for x and y plane

sobel_magnitude= cv2.convertScaleAbs(sobel_magnitude) #converting back to units for readable output

cv2.imshow("Original",img)
cv2.imshow("Sobelx", cv2.convertScaleAbs(sobelx))  #converting back to units for readable output as well as printing it for x axis
cv2.imshow("Sobely", cv2.convertScaleAbs(sobely))   #converting back to units for readable output as well as printing it for y axis


cv2.waitKey(0)
cv2.destroyAllWindows


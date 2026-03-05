import numpy as np 
import cv2

cap= cv2.VideoCapture(0)  #capture video camera 1 

width = int(cap.get(3))  #3 is width and 4 is height use documentation from opencv to check which nt value refers to which default function
height = int(cap.get(4))    
while True: 
    ret, frame= cap.read() #read the camera
    smaller_frame= cv2.resize(frame, (0,0) , fx=0.5, fy=0.5)
    image =np.zeros(frame.shape,np.uint8)
    #you cnanot rotate this image 90 degrees or 270degrees since that will chagnge the width and the height of the image which wont match with the alyout of the image hence you can only rotate it to 90 degrees
    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180) 
    
    
    image[height//2:, :width//2] = smaller_frame
    cv2.rotate(smaller_frame, cv2.ROTATE_90_CLOCKWISE)
    image[:height//2, width//2:] = smaller_frame
    cv2.rotate(smaller_frame, cv2.ROTATE_90_CLOCKWISE)
    image[height//2:, width//2:] = smaller_frame
    
    
    cv2.imshow('frame', image) #create the frame
    
    if cv2.waitKey(1) == ord('q'): #return ascii value of the key if pressed within 1ms
        break

cap.release()  #stop using the camera

cv2.destroyAllWindows()

import cv2
import numpy as np 

cap= cv2.VideoCapture(0)

while(True):
    ret,frame= cap.read()
    width= int(cap.get(3))
    height= int(cap.get(4))
    
    hsv= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #convert from bgr to hsv
    #initialize 2 numpy arrays to storet the values of the color that we want to extract
    lower_blue= np.array([90,50,50])   #light blue
    upper_blue= np.array([130,255,255]) #dark blue
    
    #creating mask
    mask= cv2.inRange(hsv,lower_blue,upper_blue) #this will only return pixels that are in the range of the  colors i gave above, the other pixels will be completely blacked out
    result =cv2.bitwise_and(hsv,hsv,mask=mask)
    
    cv2.imshow('nigger', result)
    
    if cv2.waitKey(1)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


#CUSTOM COLOR PICKER
# BGR_COLOR= np.array([[[255,0,0]]])
#     x = cv2.cvtColor(BGR_COLOR,cv2.COLOR_BGR2HSV)
#     x[0][0]
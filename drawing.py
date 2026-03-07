import cv2

cap= cv2.VideoCapture(0)

while True:
    ret, frame= cap.read()
    width= int(cap.get(3))
    height= int(cap.get(4))
                        #coordinates of img
    img = cv2.line(frame, (0,0),(width,height), (255,0,0),10) #this is the way you can draw in cv
    #pull image   (#image name)                 #color of image and thickness
    
    
    
    cv2.imshow('frame', img) #create the frame
    
    if cv2.waitKey(1) == ord('q'): #return ascii value of the key if pressed within 1ms
        break
   
   
cap.release() 
cv2.destroyAllWindows
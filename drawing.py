import cv2

cap= cv2.VideoCapture(0)

while True:
    ret, frame= cap.read()
    width= int(cap.get(3))
    height= int(cap.get(4))
                        #coordinates of img
    img = cv2.line(frame, (0,0),(width,height), (255,0,0),10) #this is the way you can draw in cv
    #pull image   (#image name)                 #color of image and thickness
    
    #drawing rectangles
    #to draw a rectangle the syntax is the same as a line just we need to pass
    #img = cv2.rectangle(name of image, left top coordinate, right bottom coordinate, color, thickness)
    
    ##FOR SHAPE TO BE COMPLETELY FILLED MAKE THICKNESS -1   
    img = cv2.rectangle(img, (0,0), (100,100), (255,0,0),-1)
    
    
    #drwaing circle
    # img = cv2.circle(frame name, center, radius,color,thickness)
    img = cv2.circle(img, (int(width/2),int(height/2)),250,(250,0,0), 10)
    
    #writing text
    font =cv2.FONT_HERSHEY_COMPLEX
    #cv2.putText(img, text, org, fontFace, fontScale, color, thickness, lineType)
    img =cv2.putText(img,"I LOVE FAT COCKS", (100,100),font,1,(0,0,0),4,cv2.LINE_AA)
    
    cv2.imshow('frame', img) #create the frame
    
    if cv2.waitKey(1) == ord('q'): #return ascii value of the key if pressed within 1ms
        break
   
   
cap.release() 
cv2.destroyAllWindows
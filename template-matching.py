import cv2
import numpy as np 

cap = cv2.VideoCapture(0)

img = cv2.resize(cv2.imread('soccer_practice.jpg', 0), (0,0), fx=0.5, fy=0.5)
template = cv2.resize(cv2.imread('shoe.PNG', 0),(0,0),fx=0.5,fy=0.5)



h,w = template.shape #this si to extract the height and weight of a grayscale image
#if this would have been a colored image it would also have the parameter of channel so (h,w,c) where c would be teh color of the image

#methods of template matching
methods = [
    cv2.TM_CCOEFF,
    cv2.TM_CCOEFF_NORMED,
    cv2.TM_CCORR,
    cv2.TM_CCORR_NORMED,
    cv2.TM_SQDIFF,
    cv2.TM_SQDIFF_NORMED
]

for method in methods:
    img2 = img.copy()
    
    result= cv2.matchTemplate(img2,template,method)
    # #template matchingworks by 
    # 1 traversal = W-w+1, H-h+1
    # where W is width of Image, w is size of template and we will traverse through this one by one
    # whichever gives the highest match is used as the best template 
    # output will be in form of an output array
    
    #checking values now
    min_val,max_val,min_loc,max_loc= cv2.minMaxLoc(result)
    #this will check the result array and return us the value of minimum maximum and their location in the image
    
    print(min_loc,max_loc)
    
    if method in [cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]: #if the template is matched using these 2 methods the best value is given by the minimum value of lcoation
        location = min_loc 
    else:
        location= max_loc #rest all template matching methods will give max value as correct position
        
    bottom_right= (location[0]+w, location[1]+h)
    cv2.rectangle(img2,location,bottom_right,255,5)
    
    cv2.imshow('nigger',img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows
    
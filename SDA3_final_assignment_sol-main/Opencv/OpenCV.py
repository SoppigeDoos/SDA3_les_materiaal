import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    
   ret, img = cap.read()
   
   hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
   lower_blue = np.array([90, 50, 50])
   upper_blue = np.array([130, 255, 255])
   
   mask =cv2.inRange(hsv, lower_blue, upper_blue)
   
   result = cv2.bitwise_and(img, img, mask=mask)
   
   thresh = cv2.threshold(img, 127, 255, 0)
   
   
   
   cv2.imshow('image', result)
   
   key = cv2.waitKey(1)
   if key == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break
    

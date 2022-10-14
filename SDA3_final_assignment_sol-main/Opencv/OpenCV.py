import cv2
from cv2 import findContours
from cv2 import RETR_TREE
from cv2 import drawContours
from cv2 import CHAIN_APPROX_NONE
import numpy as np

cap = cv2.VideoCapture(1)
screens = 0

while screens < 6:
   ret, img = cap.read()
   
   RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
   lower_red = np.array([128, 53, 50])
   upper_red = np.array([255, 123, 100])
   mask =cv2.inRange(RGB, lower_red, upper_red)

   thresh, image_edges = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)
   
   contours, hierarchy = cv2.findContours(image_edges, cv2.RETR_TREE, CHAIN_APPROX_NONE)
   cv2.drawContours(img, contours, -1, (200, 0, 200), 2)
   
   M = cv2.moments(image_edges)
   if M["m00"] != 0: 
      cX = int(M["m10"] / M["m00"])
      cY = int(M["m01"] / M["m00"])
   else:
      cX, cY = 0, 0
   
   cv2.circle(img, (cX, cY), 5, (255, 255, 255), -1)
   
   cv2.imshow('image', img)
   
   screens = screens +1
   print(cX, "\n")
   print(cY, "\n")
   
   key = cv2.waitKey(1)
   if key == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break
    

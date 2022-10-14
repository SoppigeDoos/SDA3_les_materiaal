import threading

from cv2 import CAP_XIAPI
import DoBotArm as Dbt 
import time
from serial.tools import list_ports

import cv2
from cv2 import findContours
from cv2 import RETR_TREE
from cv2 import drawContours
from cv2 import CHAIN_APPROX_NONE
import numpy as np


def port_selection():
    # Choosing port
    available_ports = list_ports.comports()
    print('Available COM-ports:')
    for i, port in enumerate(available_ports):
        print(f"  {i}: {port.description}")

    choice = int(input('Choose port by typing a number followed by [Enter]: '))
    return available_ports[choice].device

def homing_prompt():
    while (True):
        response = input("Do you wanna home? (y/n)")
        if(response == "y") :
            return True
        elif (response == "n"):
            return False
        else:
            print("Unrecognised response")

#def Track():
#    cap = cv2.VideoCapture(1)
#    screens = 0
#
#    while screens < 10:
#       ret, img = cap.read()
#    
#       RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#       lower_blue = np.array([128, 53, 50])
#       upper_blue = np.array([255, 123, 100])
#       mask =cv2.inRange(RGB, lower_blue, upper_blue)
#
#       thresh, image_edges = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)
#    
#       contours, hierarchy = cv2.findContours(image_edges, cv2.RETR_TREE, CHAIN_APPROX_NONE)
#       cv2.drawContours(img, contours, -1, (200, 0, 200), 2)
#    
#    M = cv2.moments(image_edges)
#    if M["m00"] != 0: 
#        cX = int(M["m10"] / M["m00"])
#        cY = int(M["m01"] / M["m00"])
#    else:
#        cX, cY = 0, 0
#    
#    cv2.circle(img, (cX, cY), 5, (255, 255, 255), -1)
#    cv2.imshow('image', img)
#    
#    screens = screens +1
#    print(cX, "\n")
#    print(cY, "\n")
#    return cX, cY

#--Main Program--
def Main():
    #List selected ports for selection
    port = port_selection()
        
    # Preprogrammed sequence
    homeX, homeY, homeZ = 21, 205, 30
    print("Connecting")
    print("Homing")
    ctrlBot = Dbt.DoBotArm(port, homeX, homeY, homeZ, home = True) #Create DoBot Class Object with home position x,y,z
    
    x = 293 - 297
    y = 161 - 358
    ctrlBot.moveArmXY(x, y)
    print("Disconnecting")
    
if __name__ == "__main__":
    Main()

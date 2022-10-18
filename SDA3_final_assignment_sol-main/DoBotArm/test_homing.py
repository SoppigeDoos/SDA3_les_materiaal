import threading

from cv2 import CAP_XIAPI
import DoBotArm as Dbt 
import time
from serial.tools import list_ports

import OpenCV


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

#--Main Program--
def Main():
    #List selected ports for selection
    port = port_selection()
        
    # Preprogrammed sequence
    homeX, homeY, homeZ = 0, 210, 0
    print("Connecting")
    print("Homing")
    ctrlBot = Dbt.DoBotArm(port, homeX, homeY, homeZ, home = True) #Create DoBot Class Object with home position x,y,z
    
    x = 100
    y = 210
    ctrlBot.moveArmXY(x, y)
    print("Disconnecting")
    
if __name__ == "__main__":
    Main()

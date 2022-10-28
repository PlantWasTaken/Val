import win32api 
import time 
from PIL import ImageGrab

state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128 
n = 0 
while True: 
    a = win32api.GetKeyState(0x01) 
 
    if a != state_left:  # Button state changed 
        state_left = a 
        if a < 0: 
            im = ImageGrab.grab()
            im.save("SHOOT" + str(n) + ".png")
            n = n + 1


    time.sleep(0.001)
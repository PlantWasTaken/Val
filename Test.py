import time as t
import keyboard
from PIL import ImageGrab
import mouse
import os

xy_pos = (960, 540)
x1 = xy_pos[0]-6
x2 = xy_pos[0]+6
y1 = xy_pos[1]-2
y2 = xy_pos[1]+2

for i in range(5):
    print("PRIME")

def switch():
    return keyboard.is_pressed('left alt')

n = 0
def find_pxl():
    global n
    igmr = ImageGrab.grab(bbox=(x1,y1,x2,y2))


    for i in range(x2-x1):    # for every col:
        for j in range(y2-y1):    # For every row
        
            pxl = igmr.getpixel(tuple(eval(str(i) + ", " + str(j))))
            

            if(240 < pxl[0] and 240 < pxl[1] and 125 > pxl[2]):
                g = ImageGrab.grab()
                mouse.click('left')
                g.save("g" + str(n) + ".png")
                n = n + 1
                t.sleep(0.3)
                return
            else:
                pass

on = False #0 off, 1 on    
while(True):
    if(switch()): #on
        on = not on
        t.sleep(1)

    if(on == True):
        os.system('cls')
        print("ON")
        find_pxl()

    if(on == False):
        os.system('cls')
        print("OFF")
        
    #find_pxl()   
    

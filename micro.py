from keyboard import read_key as pressed 
from time import sleep, time as timer
from pynput import keyboard, mouse
from data import data
import cv2, mss, numpy

left, right = mouse.Button.left, mouse.Button.right
mouse, keyboard= mouse.Controller(),keyboard.Controller()
last_move = "w"
is_turet = False

def loadImages(turret = False):
    images = {}
    if turret:
        images["turret"] = turret_template = cv2.imread('Bots/bots/screens/turret_template.png')
    return images
   
images = loadImages(turret=True)   
        
def match(object):
    sct = mss.mss()
    scr = numpy.array(sct.grab(data.img_detection["dimensions"]))
    # Cut off alpha
    scr_remove = scr[:,:,:3]

    result = cv2.matchTemplate(scr_remove, images[object], cv2.TM_CCOEFF_NORMED)
    
    _, max_val, _, _ = cv2.minMaxLoc(result)
    if max_val > 0.75:
        return True
    return False

def wait(time=0.03):
    sleep(time)
    
def click(button=left):
    mouse.click(button=button)

def move(pos):
    mouse.position = (pos[0],pos[1])

def move_click(pos,button=left):
    mouse.position = (pos[0],pos[1])
    wait()
    mouse.click(button=button)
    
def selectKey(keys):
    for key in keys:
        keyboard.press(key)
        keyboard.release(key)
        
def build(positions, multi = True):
    if multi:
        for pos in positions:
            move_click(pos)
    else:
        move_click(positions)

def open(position=None, slot_pos=data.slot_pos["turret"]):
    if position != None:
        move(position)
        wait()
    click()
    wait()
    move(slot_pos)
    wait()

def feed_slot(ammount=5, slot_pos = None):
    if slot_pos != None:
        move(slot_pos)
        wait()
    for i in range(ammount):
        click(right)
        
def build_turrets(positions,multi=True,ammo=5):
    selectKey(["q","1"])
    build(positions, multi)
    wait()
    selectKey("2")
    for pos in positions:
        move(pos)
        wait(0.07)        
        if match("turret"):
            #print("found")
            open()
            wait()
            feed_slot()
            selectKey("'")
            wait()
        #else:
            #print("not found")
while True:
    pressed_key = pressed()  
    if pressed_key in data.move_keys:
        last_move = pressed_key
        
    if pressed_key == ".":
        keyboard.release(last_move)
        start = timer()
        build_turrets(data.turrets_build[last_move])
        end = timer()
        print(end-start)

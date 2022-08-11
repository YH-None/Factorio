from keyboard import read_key as pressed 
from time import sleep, time as timer
from pynput import keyboard, mouse
from data import center, tile_size, slots
from img_match import imgs, match, images

left, right = mouse.Button.left, mouse.Button.right
mouse, keyboard= mouse.Controller(),keyboard.Controller()

def wait(time=0.03):
    sleep(time)
    
def tile_pos(pos):
    return [center[0]+tile_size*pos[0],center[1]+tile_size*pos[1]]
    
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
        
def build(pos):
    move_click(pos)
        
def open(pos=None):
    if pos != None:
        move_click(pos)
    else:
        click()

def feed_slot(ammount=5, slot_name = "default"):
    move(slots[slot_name])
    wait()
    for i in range(ammount):
        click(right)
         
def build_turrets(tile_positions):
    positions = []
    for pos in tile_positions:
        positions.append(tile_pos(pos))
    selectKey(["q","1"])
    for pos in positions:
        build(pos)
        wait()
    selectKey(["2"])
    for pos in positions:
        move(pos)
        wait(0.1)
        if match("turret",images):
            click()
            wait()
            feed_slot()
            selectKey(["'"])  

def layout(d, key):
    return {"w":[[-d,-d],[d,-d]],"s":[[-d,d],[d,d]],"a":[[-d,-d],[-d,d]],"d":[[d,-d],[d,d]]}[key]
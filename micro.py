from keyboard import read_key as pressed 
from time import sleep, time as timer
from pynput import keyboard
from pynput import mouse
import pixel_pos

left, right = mouse.Button.left, mouse.Button.right
mouse, keyboard= mouse.Controller(),keyboard.Controller()

def wait(time=0.05):
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

def open(position, slot_pos):
    move(position)
    wait()
    click()
    wait()
    move(slot_pos)
    wait()

def feed_slot(ammount=5):
    for i in range(ammount):
        click(right)
        
def build_turrets(positions,multi=True,ammo=5):
    selectKey(["q","1"])
    build(positions, multi)
    wait()
    selectKey("2")
    for pos in positions:
        open(pos,pixel_pos.slot_pos["turret"])
        wait()
        feed_slot()
        selectKey("'")
        wait()

while True:
    if pressed() == ".":
        #start = timer()
        build_turrets(pixel_pos.turrets_build["w"])
        #end = timer()
        #rint(end-start)
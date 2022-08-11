import data
import control as c
from keyboard import read_key as pressed, release
from time import time as timer, sleep
from pynput import keyboard, mouse
import img_match

distance = 3
last_move = "w"

while True:
    pressed_key = pressed()  
    if pressed_key in data.move_keys:
        last_move = pressed_key
        
    if pressed_key == ".":
        release(last_move)
        c.build_turrets(c.layout(distance,last_move))
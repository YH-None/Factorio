import data
import control as c
from keyboard import read_key as pressed, release
from time import time as timer, sleep
from pynput import keyboard, mouse
import img_match

if pressed() == ".":
    keyboard.press("w")
import dxcam
import mss
import cv2
from time import time, sleep
import pyautogui

pyautogui.PAUSE = 0
camera = dxcam.create()
sct = mss.mss()
dimensions = {
        'left': 2305,
        'top': 469,
        'width': 2379,
        'height': 493
}

turret_template = cv2.imread('Bots/bots/screens/turret_template.png',cv2.TM_CCOEFF)

w = turret_template.shape[1]
h = turret_template.shape[0]

fps_time = time()
while True:
    scr = camera.grab(region=(2305, 469, 2379, 493))
    # Cut off alpha
    scr_remove = scr[:,:,:3]

    result = cv2.matchTemplate(scr_remove, turret_template, cv2.TM_CCOEFF_NORMED)
    
    _, max_val, _, _ = cv2.minMaxLoc(result)
    if max_val > 0.75 or False:
        print("found")
        break
      
    print('FPS: {}'.format(1 / (time() - fps_time)))
    sleep(0.02)
    fps_time = time()
    
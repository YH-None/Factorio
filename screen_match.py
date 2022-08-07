import mss
import cv2
import numpy
from time import time, sleep
import pyautogui

pyautogui.PAUSE = 0

def loadImages(turret = False):
    images = {}
    if turret:
        images["turret"] = cv2.imread('Bots/bots/screens/turret_template.png')
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

dimensions = {
        'left': 2305,
        'top': 469,
        'width': 2379,
        'height': 493
}


fps_time = time()
while True:
        img = loadImages(True)
        if match(img):
                print("Found")
    
    #print('FPS: {}'.format(1 / (time() - fps_time)))
    fps_time = time()

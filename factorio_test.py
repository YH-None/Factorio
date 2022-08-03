import pyautogui 
import cv2
import mss
import time
import easygui
import win32gui, win32con
import numpy as np
"""
# check point.
while True:
        print (pyautogui.position ())
"""
"""
# get screenshot.
def get_screenshot ():
        win32gui.SetForegroundWindow(1575214)
        img = mss.mss ()
        screenshot = img.shot (mon = -1, output = "screenshot.png")
        easygui.msgbox ("done")
get_screenshot ()
"""
img = cv2.imread ("screenshot.png", -1)

#cv2.imshow ("img", img)
img = cv2.cvtColor (img, cv2.COLOR_BGR2HSV)
cv2.imwrite ("1.png", img)

# 高斯模糊处理
gs_img = cv2.GaussianBlur (img, (5, 5), 0)
cv2.imwrite ("gs_img.png", gs_img)

# 图片腐蚀
img = cv2.erode (gs_img, None, iterations = 6)

# 去除背景
img = cv2.inRange (img, np.array ([0, 0, 0]), np.array ([0, 100, 320]))
cv2.imwrite ("a.png", img)

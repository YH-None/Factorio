import mss
import mss.tools
from keyboard import read_key as pressed 
from time import sleep

location = "C:/Users/path"
screen_w,screen_h = 2560,1080

#top left [0,0], bottom right[screen size]
name_d_x, name_d_y = 252, 472
name_w,name_h = 96, 20

screshot_pos = [[screen_w-name_d_x, name_d_y],[screen_w-name_d_x+name_w,name_d_y+name_h]]

def wait(time = 0.5):
    sleep(time)
    
def save_building_name(b_name):
    with mss.mss() as sct:
        # The screen part to capture
        monitor = {"top": name_d_y, "left": screen_w-name_d_x, "width": name_w, "height": name_h}
        output = location + b_name + ".png"
        
        # Grab the data
        sct_img = sct.grab(monitor)

        # Save to the picture file
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)

while True:
    if pressed() == ".":
        save_building_name("Tree")
        break

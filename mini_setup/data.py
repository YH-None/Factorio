#screen size
screen_w,screen_h = 2560,1080
#top left [0,0], bottom right[screen size]

#name position
tile_size = 32
center = [screen_w//2,screen_h//2]
name_d_x, name_d_y = 252, 472
name_w,name_h = 96, 20
name_monitor = {"top": name_d_y, "left": screen_w-name_d_x, "width": name_w, "height": name_h}

#slot positions
slots = {"default":[1320, 520]}

move_keys = ["w","s","a","d"]
directions = {"w":[[-1,-1],[1,-1]],"s":[[-1,1],[1,1]],"a":[[-1,-1],[-1,1]],"d":[[1,-1],[1,1]]}
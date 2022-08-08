import cv2, mss, numpy, data

def imgs(turret = False):
    images = {}
    if turret:
        images["turret"] = cv2.imread('Bots/bots/screens/turret.png')
    return images

def match(obj_name, images):
    sct = mss.mss()
    scr = numpy.array(sct.grab(data.name_monitor))
    # Cut off alpha
    scr_remove = scr[:,:,:3]

    result = cv2.matchTemplate(scr_remove, images[obj_name], cv2.TM_CCOEFF_NORMED)
    
    _, max_val, _, _ = cv2.minMaxLoc(result)
    if max_val > 0.95:
        print(max_val)
        return True
    return False

images = imgs(turret=True)

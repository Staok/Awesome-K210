import video,time,lcd

lcd.init()

#改变方向，可选
#lcd.direction(lcd.YX_LRUD)

v = video.open("/sd/capture.avi")
#print(v)
v.volume(50)
while True:
    if v.play() == 0:
        print("play end")
        break
    
v.__del__()


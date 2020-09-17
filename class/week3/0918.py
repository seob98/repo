from pico2d import *
import os

os.chdir('E:/python/0914')

open_canvas()

gra = load_image('grass.png')
ch = load_image('run_animation.png')

x = 0
frame_index = 0
while x < 800:
    clear_canvas()
    gra.draw(400,30)
    ch.clip_draw(sx,0,100,100,x,85)
    update_canvas()
    

    evts = get_events()

    x += 2

    frame_index = (frame_index + 1) % 8
    
    delay(0.01)

    



close_canvas()

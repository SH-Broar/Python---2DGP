from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 200
y = 200
# fill here
while(1):
    for t in range(0,360):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(400 + 200*math.cos(t),300 + 200*math.sin(t))
        delay(0.05)
    
close_canvas()

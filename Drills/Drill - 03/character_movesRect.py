from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 20
y = 90
# fill here
while(1):
    while(x < 780):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = x + 2
        delay(0.002)
    while(y < 530):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y = y + 2
        delay(0.002)
    while(x > 20):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = x - 2
        delay(0.002)
    while(y > 90):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y = y - 2
        delay(0.002)
    
close_canvas()

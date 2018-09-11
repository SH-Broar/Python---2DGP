from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90
# fill here
while(1):
    while(x < 780):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = x + 5
        delay(0.02)
    while(y < 530):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y = y + 5
        delay(0.02)
    while(x > 20):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = x - 5
        delay(0.02)
    while(y > 90):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y = y - 5
        delay(0.02)
    while(x < 400):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = x + 5
        delay(0.02)
    for t in range(0,62):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(400 + 200*math.sin(t/10),300 + -200*math.cos(t/10))
        delay(0.05)
    
close_canvas()

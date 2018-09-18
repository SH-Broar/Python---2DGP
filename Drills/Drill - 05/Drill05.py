from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 100
y = 50
# init of global var


def character_point(destination_x, destination_y):
    global x
    global y
    while x != destination_x or y != destination_y:
        if x < destination_x:
            x += 1
        if y < destination_y:
            y += 1
        if x > destination_x:
            x -= 1
        if y > destination_y:
            y -= 1
        character_rend()
    pass


def character_rend():
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    delay(0.01)


DestinationList = [203, 535, 132, 243, 535, 470, 477, 203, 715, 136, 316, 225, 510, 92, 692, 518, 682, 336, 712, 349]


while True:
    index = 0
    character_point(DestinationList[index], DestinationList[index+1])
    index = index + 2



close_canvas()

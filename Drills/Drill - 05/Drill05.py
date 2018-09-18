from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 100
y = 50

d1 = False
d2 = False
d3 = False
d4 = False
# init of global var


def character_point(destination_x, destination_y):
    global x
    global y
    global d1
    global d2
    global d3
    global d4
    while x != destination_x or y != destination_y:
        d1 = False
        d2 = False
        d3 = False
        d4 = False

        if x < destination_x:
            x += 1
            d1 = True
        if y < destination_y:
            y += 1
            d2 = True
        if x > destination_x:
            x -= 1
            d3 = True
        if y > destination_y:
            y -= 1
            d4 = True
        character_rend()
    pass


def character_rotate_rend():
    rad = 0
    if d1 is True and d2 is False and d4 is False:
        rad = 0
    if d3 is True and d2 is False and d4 is False:
        rad = 180
    if d2 is True and d1 is False and d3 is False:
        rad = 90
    if d4 is True and d1 is False and d3 is False:
        rad = 270
    if d1 is True and d2 is True:
        rad = 45
    if d1 is True and d4 is True:
        rad = 135
    if d3 is True and d2 is True:
        rad = 315
    if d3 is True and d4 is True:
        rad = 225

    character.rotate_draw(math.radians(rad), x, y)


def character_rend():
    clear_canvas()
    grass.draw(400, 30)
    # character.draw(x, y)
    character_rotate_rend()
    delay(0.001)
    update_canvas()


DestinationList = [203, 535, 132, 243, 535, 470, 477, 203, 715, 136, 316, 225, 510, 92, 692, 518, 682, 336, 712, 349]
index = 0

while True:
    character_point(DestinationList[index], DestinationList[index+1])
    index = index + 2
    if index >= 20:
        index = 0

close_canvas()

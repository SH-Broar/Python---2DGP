from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')


def character_movetopoint(destX, destY):

    pass


DestinationList = [203, 535, 132, 243, 535, 470, 477, 203, 715, 136, 316, 225, 510, 92, 692, 518, 682, 336, 712, 349]


while True:
    index = 0
    character_movetopoint(DestinationList[index],DestinationList[index+1])
    index = index + 2


close_canvas()

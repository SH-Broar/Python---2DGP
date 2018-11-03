import random
import json
import os

from pico2d import *
import game_framework
import game_world

import boy
from grass import Grass
from Blocks import Blocks

name = "MainState"

by = None
BGM = None
TimeCut = []

class Stage1_Bgm:
    def __init__(self):
        self.bgm = load_music('1City.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

def enter():
    global by, BGM
    #파일에서 데이터 받아와서 미리 저장하기
    by = boy.Boy()
    grass = Grass()
    game_world.add_object(grass, 0)
    game_world.add_object(by, 2)
    mapper()
    if BGM is None:
        BGM = Stage1_Bgm()
    else:
        BGM.bgm.repeat_play()

def mapper():
    global TimeCut
    input = open("tile\\map.txt", "rt")
    A = []
    LineOfFile = 0
    for line in input:
        A.append(line.strip())
        LineOfFile += 1
    input.close()
    for line in range(LineOfFile):
        if line % 13 == 0:
            TimeCut.append(float(A[line]))
        else:
            for b in A[line]:
                x = int(b)
                boy.Mapper.append(x)

    TimeCut.append(999) # type Music Length


def MakeMap():
    global TimeCut
    xl = 0
    if get_time() < TimeCut[boy.order]:
        pass
    else:
        boy.order += 1
        # block class make and mapping in here
        # by using order in Mapper, can print block in real time.
        game_world.remove_object_by_line(1)
        for yLine in range(0, 12):
            for xLine in range(0, 20):
                tile = Blocks(xLine * 50 + 25, 600 - (yLine+1) * 50 + 25, boy.Mapper[(boy.order-1)*240 + xl])
                game_world.add_object(tile, 1)
                xl += 1



def exit():
    global BGM
    game_world.clear()
    BGM = None

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            by.handle_event(event)


def update():
    MakeMap()
    for game_object in game_world.all_objects():
        game_object.update()
    delay(0.01)
    # fill here



def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()







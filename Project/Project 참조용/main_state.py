import random
import json
import os

from pico2d import *
import game_framework
import game_world

from boy import Boy
from grass import Grass


name = "MainState"

boy = None

BGM = None

class Stage1_Bgm:
    def __init__(self):
        self.bgm = load_music('1City.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

def enter():
    global boy, BGM
    #파일에서 데이터 받아와서 미리 저장하기
    boy = Boy()
    grass = Grass()
    game_world.add_object(grass, 0)
    game_world.add_object(boy, 1)
    if BGM is None:
        BGM = Stage1_Bgm()
    else:
        BGM.bgm.repeat_play()


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
            boy.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()
    delay(0.01)
    # fill here


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()







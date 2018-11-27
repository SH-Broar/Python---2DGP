import random
import json
import pickle
import os

from pico2d import *
import game_framework
import game_world

import main_state

boy = None
rankdata = []
data = []

name = "RankingState"
font = None
menu = None

def enter():
    global menu,font,rankdata, data
    if font is None:
        font = load_font('ENCR10B.TTF', 20)
    menu = load_image('ranking.png')
    hide_cursor()
    hide_lattice()
    with open('ranking.json','r')as f:
        data_list = json.load(f)

    data = data_list["Ranking"]
    data.sort()

def exit():
    global menu
    del menu

def pause():
    pass

def resume():
    pass

def get_boy():
    return boy

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()

def update():

    pass

def draw():
    global font, data
    clear_canvas()
    menu.draw(get_canvas_width()//2, get_canvas_height()//2)

    tick = 10
    if len(data) < 10:
        for i in range(1,len(data)):
            font.draw(50, 50 + i*50, str(data[i]), (0, 0, 0))
        update_canvas()
    else:
        for i in range(1, 10):
            font.draw(50, 50 + i * 50, str(data[i]), (0, 0, 0))
        update_canvas()








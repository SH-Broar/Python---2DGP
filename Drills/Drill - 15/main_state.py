import random
import json
import pickle
import os

from pico2d import *
import game_framework
import game_world

import world_build_state
import ranking_state

name = "MainState"


def collide(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

boy = None

def enter():
    # game world is prepared already in world_build_state
    global boy
    boy = world_build_state.get_boy()
    pass

def exit():
    game_world.clear()

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
            game_framework.change_state(world_build_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_s:
            game_world.save()
        else:
            boy.handle_event(event)


def update():
    global boy
    for game_object in game_world.all_objects():
        game_object.update()
    for game_object in game_world.all_objects():
        if collide(boy, game_object):
            print(game_object.__name__)
            if game_object.__name__ is 'zombie':
                game_world.remove_object(game_object)

                with open('ranking.json') as f:
                    rankingdata = json.load(f)
                tempdata = rankingdata["Ranking"]
                tempdata.append(get_time() - boy.start_time)

                rankingdata["Ranking"] = tempdata
                json.dumps(rankingdata)
                with open('ranking.json', 'w', encoding="utf-8") as make_file:
                    json.dump(rankingdata, make_file, ensure_ascii=False, indent="\t")

                game_framework.change_state(ranking_state)
                pass


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()







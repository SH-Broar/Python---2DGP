import random
import json
import os

from pico2d import *

import game_framework
import title_state
import pause_state



name = "MainState"

player = None
grass = None
font = None


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Player:
    def __init__(self):
        self.x, self.y = 50, 90
        self.jump = 150
        self.jumpHeight = 0
        self.dir = 0 # 0 up 1 down
        self.frame = 0
        self.image = load_image('Player\\player.png')
        self.dir = 1

    def update(self):
        if self.dir == 0:
            self.jumpHeight += 1
            if self.jumpHeight >= self.jump:
                self.dir = 1
        else:
            self.jumpHeight -= 1
            if self.jumpHeight <= 0:
                self.dir = 0
        pass

    def draw(self):
        self.image.draw(self.x,self.y + self.jumpHeight,50,50)

    def setPosition(self,x,y):
        self.x += x
        self.y += y


def enter():
    global player, grass
    if (player == None):
        player = Player()
        grass = Grass()


def exit():
    global player, grass
    del(player)
    del(grass)


def pause():
    pass



def resume():
    pass


def handle_events():
    global player
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
            game_framework.push_state(pause_state)

        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT and player.jumpHeight < 20:
            player.setPosition(-50,0)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT and player.jumpHeight < 20:
            player.setPosition(50, 0)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP and player.jumpHeight < 20:
            player.setPosition(0, 50)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_DOWN and player.jumpHeight < 20:
            player.setPosition(0, -50)


def update():
    player.update()


def draw():
    clear_canvas()
    grass.draw()
    player.draw()
    update_canvas()






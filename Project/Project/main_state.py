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

BGM = None

class Stage1_Bgm:
    def __init__(self):
        self.bgm = load_music('1City.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Player:
    def __init__(self):
        self.x, self.y = 50, 80
        self.jump = 139
        self.jumpHeight = 0
        self.dir = 0 # 0 up 1 down
        self.frame = 0
        self.image = load_image('Player\\player.png')
        self.dir = 1
        self.CtrlKeyDown = 1

    def update(self,fDeltaTime):
        if self.dir == 0:
            self.jumpHeight += 1970 / ((self.jumpHeight+100)/50) * fDeltaTime
            if self.jumpHeight >= self.jump:
                self.dir = 1
        else:
            self.jumpHeight -= 1975 / ((self.jumpHeight+100)/50) * fDeltaTime
            self.jumpHeight -= 10*fDeltaTime
            if self.jumpHeight <= 0:
                self.dir = 0
                self.jumpHeight = 0
        pass

    def draw(self):
        self.image.draw(self.x,self.y + self.jumpHeight,50,50)

    def setPosition(self,x,y):
        self.x += x
        self.y += y

    def pressKey(self):
        pass


def enter():
    global player, grass, BGM
    if (player == None):
        player = Player()
        grass = Grass()
    if BGM is None:
        BGM = Stage1_Bgm()
    else:
        BGM.bgm.repeat_play()


def exit():
    global player, grass, BGM
    del(player)
    del(grass)
    BGM = None


def pause():

    pass



def resume():
    pass



def handle_events(fDeltaTime):
    global player
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
            game_framework.push_state(pause_state)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LCTRL):
            player.CtrlKeyDown = 3
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LCTRL):
            player.CtrlKeyDown = 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT and player.jumpHeight < 50:
            player.setPosition(-50 * player.CtrlKeyDown,0)
            player.pressKey()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT and player.jumpHeight < 50:
            player.setPosition(50 * player.CtrlKeyDown, 0)
            player.pressKey()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP and player.jumpHeight < 50:
            player.setPosition(0, 50 * player.CtrlKeyDown)
            player.pressKey()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_DOWN and player.jumpHeight < 50:
            player.setPosition(0, -50 * player.CtrlKeyDown)
            player.pressKey()


def update(fDeltaTime):
    player.update(fDeltaTime)


def draw(fDeltaTime):
    clear_canvas()
    grass.draw()
    player.draw()
    update_canvas()






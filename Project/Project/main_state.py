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
        self.image = load_image('Player\\player.png')
        #
        self.jump = 139
        self.jumpHeight = 0
        self.dir = 0 # 0 up 1 down
        #
        self.frame = 0

        #
        self.dir = 1
        self.rotatedir = 0
        #
        self.moving = 0
        self.movement = 0
        self.movementy = 0
        #
        self.CtrlKeyDown = 1

    def move(self, fDeltaTime):
        if self.moving == 1:
            self.movement -= 112 * fDeltaTime* self.CtrlKeyDown
            if self.movement <= -50 * self.CtrlKeyDown:
                self.movement = 0
                self.x -= 50 * self.CtrlKeyDown
                self.moving = 0
                self.rotatedir -= 1 * self.CtrlKeyDown
                player.CtrlKeyDown = 1
                if self.rotatedir <= -4:
                    self.rotatedir += 4
            pass
        elif self.moving == 2:
            self.movement += 112 * fDeltaTime * self.CtrlKeyDown
            if self.movement >= 50 * self.CtrlKeyDown:
                self.movement = 0
                self.x += 50 * self.CtrlKeyDown
                self.moving = 0
                self.rotatedir += 1 * self.CtrlKeyDown
                player.CtrlKeyDown = 1
                if self.rotatedir >= 4:
                    self.rotatedir -= 4
            pass
        elif self.moving == 3:
            self.movementy += 112 * fDeltaTime * self.CtrlKeyDown
            if self.movementy >= 50 * self.CtrlKeyDown:
                self.movementy = 0
                self.y += 50 * self.CtrlKeyDown
                self.moving = 0
                self.rotatedir -= 2 * self.CtrlKeyDown
                player.CtrlKeyDown = 1
                if self.rotatedir <= -4:
                    self.rotatedir += 4
            pass
        elif self.moving == 4:
            self.movementy -= 112 * fDeltaTime * self.CtrlKeyDown
            if self.movementy <= -50 * self.CtrlKeyDown:
                self.movementy = 0
                self.y -= 50 * self.CtrlKeyDown
                self.moving = 0
                self.rotatedir += 2 * self.CtrlKeyDown
                player.CtrlKeyDown = 1
                if self.rotatedir >= 4:
                    self.rotatedir -= 4
            pass

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

        player.move(fDeltaTime)
        pass

    def draw(self):
        self.image.rotate_draw(((self.movement+ self.movementy*2)*-90/50)*3.14 / 180 - self.rotatedir*90*3.14/180,self.x + self.movement,self.y + self.jumpHeight + self.movementy,50,50)

    def setPosition(self,x,y):
        self.x += x
        self.y += y

    def pressKey(self, direction):
        if direction == 1:
            self.moving = 1
            pass
        elif direction == 2:
            self.moving = 2
            pass
        elif direction == 3:
            self.moving = 3
            pass
        elif direction == 4:
            self.moving = 4
            pass
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
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LCTRL) and player.moving == 0:
                if player.CtrlKeyDown == 3:
                    player.CtrlKeyDown = 1
                else:
                    player.CtrlKeyDown = 3
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT and player.jumpHeight < 60:
            player.pressKey(1)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT and player.jumpHeight < 60:
            player.pressKey(2)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP and player.jumpHeight < 60:
            player.pressKey(3)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_DOWN and player.jumpHeight < 60:
            player.pressKey(4)


def update(fDeltaTime):
    player.update(fDeltaTime)


def draw(fDeltaTime):
    clear_canvas()
    grass.draw()
    player.draw()
    update_canvas()






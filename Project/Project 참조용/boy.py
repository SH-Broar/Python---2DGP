import game_framework
from pico2d import *
from ball import Ball

import game_world
import random
import math

# Boy Run Speed
# fill expressions correctly
PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0/60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS*PIXEL_PER_METER)

# Boy Action Speed
# fill expressions correctly
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8



# Boy Event
RIGHT_DOWN, LEFT_DOWN, UP_DOWN, DOWN_DOWN, SPACE, TimeUp = range(6)


key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,

    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN,

    (SDL_KEYDOWN, SDLK_SPACE): SPACE
}


# Boy States

class IdleState:

    @staticmethod
    def enter(boy, event):
        boy.prevTime = get_time()

    @staticmethod
    def exit(boy, event):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame+(180*(boy.MusicBpm/60)*game_framework.frame_time)) % 180
        boy.jumpHeight = math.sin(boy.frame * 3.14 / 180) * 100
        if (boy.keyDown == True):
            boy.CtrlDown = 3
        else:
            boy.CtrlDown = 1


    @staticmethod
    def draw(boy):
        boy.image.rotate_draw(boy.angle* 3.14 / 180,boy.x, boy.y + boy.jumpHeight, 50, 50)
        if (boy.keyDown == True):
            boy.power.rotate_draw(-boy.frame* 3.14 / 360,boy.x, boy.y + boy.jumpHeight, 120, 120)


class RunState:

    @staticmethod
    def enter(boy, event):
        if event == RIGHT_DOWN:
            if boy.jumpHeight <= 30:
                if (boy.keyDown == True):
                    boy.CtrlDown = 3
                else:
                    boy.CtrlDown = 1
                boy.dir = 1
                boy.bangle = 0
                boy.exX = boy.x
            elif boy.bangle is 0:
                boy.cur_state = IdleState
                boy.cur_state.enter(boy, TimeUp)
        elif event == LEFT_DOWN:
            if boy.jumpHeight <= 30:
                if boy.keyDown == True:
                    boy.CtrlDown = 3
                else:
                    boy.CtrlDown = 1
                boy.dir = -1
                boy.bangle = 0
                boy.exX = boy.x
            elif boy.bangle is 0:
                boy.cur_state = IdleState
                boy.cur_state.enter(boy, TimeUp)
        elif event == UP_DOWN:
            if boy.jumpHeight <= 30:
                if boy.keyDown == True:
                    boy.CtrlDown = 3
                else:
                    boy.CtrlDown = 1
                boy.dir = 2
                boy.bangle = 0
                boy.exY = boy.y
            elif boy.bangle is 0:
                boy.cur_state = IdleState
                boy.cur_state.enter(boy, TimeUp)
        elif event == DOWN_DOWN:
            if boy.jumpHeight <= 30:
                if boy.keyDown == True:
                    boy.CtrlDown = 3
                else:
                    boy.CtrlDown = 1
                boy.dir = -2
                boy.bangle = 0
                boy.exY = boy.y
            elif boy.bangle is 0:
                boy.cur_state = IdleState
                boy.cur_state.enter(boy, TimeUp)

    @staticmethod
    def exit(boy, event):
        pass


    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + (180 * (boy.MusicBpm / 60) * game_framework.frame_time)) % 180
        if boy.bangle < 90 or boy. bangle > 270:
            boy.angle = (boy.angle - (90 * (boy.MusicBpm / 60) * game_framework.frame_time) * boy.dir) % 360
            boy.bangle = (boy.bangle + (90 * (boy.MusicBpm / 60) * game_framework.frame_time) * boy.dir) % 360

        boy.jumpHeight = math.sin(boy.frame * 3.14 / 180) * 100

        if boy.bangle > 90 and boy.bangle < 270: # end
        #{
            boy.exX = boy.x
            boy.exY = boy.y
            boy.angle = boy.angle - 45
            boy.angle = boy.angle - (boy.angle % 90) + 90
            boy.dir = 0
            boy.bangle = 0

            boy.cur_state = IdleState
            boy.cur_state.enter(boy,TimeUp)
        #}
        if boy.dir == 1:
            boy.x = boy.exX + boy.bangle / 90 * 51 * boy.CtrlDown
        elif boy.dir == -1:
            boy.x = boy.exX - (360 - boy.bangle) / 90 * 51 * boy.CtrlDown
        elif boy.dir == 2:
            boy.y = boy.exY + boy.bangle / 90 * 51
        elif boy.dir == -2:
            boy.y = boy.exY - (360 - boy.bangle) / 90 * 51


    @staticmethod
    def draw(boy):
        boy.image.rotate_draw(boy.angle * 3.14 / 180, boy.x, boy.y + boy.jumpHeight, 50, 50)
        if (boy.keyDown == True):
            boy.power.rotate_draw(-boy.bangle* 3.14 / 180,boy.x, boy.y + boy.jumpHeight, 120, 120)


next_state_table = {
    IdleState: {RIGHT_DOWN: RunState, LEFT_DOWN: RunState, SPACE: IdleState,
                UP_DOWN: RunState, DOWN_DOWN: RunState,TimeUp: IdleState},
    RunState: {LEFT_DOWN: RunState, RIGHT_DOWN: RunState, SPACE: RunState,
               UP_DOWN: RunState, DOWN_DOWN: RunState,TimeUp: IdleState},
}

class Boy:

    def __init__(self):
        self.x, self.y = 25, 60
        self.exX = 0
        self.exY = 0
        self.image = load_image('Player\\player.png')
        self.power = load_image('Player\\power.png')
        # Boy is only once created, so instance image loading is fine
        self.font = load_font('ENCR10B.TTF',16)
        self.dir = 0
        self.velocity = 0
        #
        self.MusicBpm = 126
        #
        self.keyDown = False
        self.teleportDir = 0
        self.CtrlDown = 1
        self.frame = 0      #점프용
        self.jumpHeight = 0
        self.bangle = 0
        self.angle = 0
        #
        self.prevTime = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def fire_ball(self):
        ball = Ball(800,200)
        game_world.add_object(ball,1)
        pass

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LCTRL):
            self.keyDown = True
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LCTRL):
            self.keyDown = False
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RCTRL):
            self.keyDown = True
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_RCTRL):
            self.keyDown = False
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LSHIFT):
            self.teleportDir = -1
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RSHIFT):
            self.teleportDir = 1
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LSHIFT):
            self.teleportDir = 0
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_RSHIFT):
            self.teleportDir = 0

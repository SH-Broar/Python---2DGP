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
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SPACE, TimeUp = range(6)


key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE
}


# Boy States

class IdleState:

    @staticmethod
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            boy.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            boy.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            boy.velocity += RUN_SPEED_PPS
        boy.prevTime = get_time()

    @staticmethod
    def exit(boy, event):
        if event == SPACE:
            boy.fire_ball()
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame+(180*(boy.MusicBpm/60)*game_framework.frame_time)) % 180
        boy.jumpHeight = math.sin(boy.frame * 3.14 / 180) * 100



    @staticmethod
    def draw(boy):
        boy.image.rotate_draw(boy.angle* 3.14 / 180,boy.x, boy.y + boy.jumpHeight, 50, 50)


class RunState:

    @staticmethod
    def enter(boy, event):
        if event == RIGHT_DOWN:
            if boy.jumpHeight <= 30:
                boy.dir = 1
                boy.bangle = 0
                boy.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            if boy.jumpHeight <= 30:
                boy.dir = -1
                boy.bangle = 0
                boy.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            boy.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            boy.velocity += RUN_SPEED_PPS



    @staticmethod
    def exit(boy, event):
        if event == SPACE:
            boy.fire_ball()
        if event == LEFT_DOWN or RIGHT_DOWN:
            boy.angle = boy.angle - 45
            boy.angle = boy.angle - (boy.angle % 90) + 90
            boy.dir = 0
            boy.bangle = 0
        if event == TimeUp:
            boy.angle = boy.angle - 45
            boy.angle = boy.angle - (boy.angle % 90) + 90
            boy.dir = 0
            boy.bangle = 0

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + (180 * (boy.MusicBpm / 60) * game_framework.frame_time)) % 180
        if boy.bangle < 90 or boy. bangle > 270:
            boy.angle = (boy.angle - (90 * (boy.MusicBpm / 60) * game_framework.frame_time) * boy.dir) % 360
        boy.bangle = (boy.bangle + (90 * (boy.MusicBpm / 60) * game_framework.frame_time) * boy.dir) % 360
        boy.x = boy.x + boy.dir * game_framework.frame_time * 50
        boy.jumpHeight = math.sin(boy.frame * 3.14 / 180) * 100

        if boy.bangle >= 110 and boy.bangle <= 250:
            boy.add_event(TimeUp)

    @staticmethod
    def draw(boy):
        boy.image.opacify(1)
        boy.image.rotate_draw(boy.angle* 3.14 / 180, boy.x, boy.y + boy.jumpHeight, 50, 50)


next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, SPACE: IdleState, TimeUp: IdleState},
    RunState: {RIGHT_UP: RunState, LEFT_UP: RunState, LEFT_DOWN: RunState, RIGHT_DOWN: RunState, SPACE: RunState, TimeUp: IdleState},
}

class Boy:

    def __init__(self):
        self.x, self.y = 50, 80
        self.image = load_image('Player\\player.png')
        # Boy is only once created, so instance image loading is fine
        self.font = load_font('ENCR10B.TTF',16)
        self.dir = 1
        self.velocity = 0
        #
        self.MusicBpm = 100
        #
        self.keyDown = False
        self.CtrlDown = 0
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
        ball = Ball(self.x, self.y + self.jumpHeight, self.dir*3)
        game_world.add_object(ball, 1)

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


import random
from pico2d import *
import game_world
import game_framework
import main_state

class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.fall_speed = random.randint(400, 1400), random.randint(300, 800), 0
        self.x += 400
        self.y += 300
    def get_bb(self):
        return self.x- main_state.boy.x - 10, self.y- main_state.boy.y - 10, self.x-main_state.boy.x + 10, self.y- main_state.boy.y + 10

    def draw(self):
        self.image.draw(self.x- main_state.boy.x, self.y- main_state.boy.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

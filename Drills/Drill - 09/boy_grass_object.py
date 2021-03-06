from pico2d import *
import random


# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Ball21:
    def __init__(self):
        self.x, self.y = random.randint(21, 779), 599
        self.dropSpeed = random.randint(4, 25)
        self.image = load_image('ball21x21.png')

    def update(self):
        if self.y > 60:
            self.y -= self.dropSpeed
        else:
            self.y = 60

    def draw(self):
        self.image.draw(self.x, self.y)


class Ball41:
    def __init__(self):
        self.x, self.y = random.randint(21, 779), 599
        self.dropSpeed = random.randint(4, 25)
        self.image = load_image('ball41x41.png')

    def update(self):
        if self.y > 70:
            self.y -= self.dropSpeed
        else:
            self.y = 70

    def draw(self):
        self.image.draw(self.x, self.y)


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)


def handle_events():
    global running
    global stop
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            if stop is True:
                stop = False
            else:
                stop = True


# initialization code
open_canvas()

ballcut = random.randint(5, 15)
team = [Boy() for i in range(11)]
ball21s = [Ball21() for i in range(ballcut)]
ball41s = [Ball41() for i in range(20-ballcut)]
grass = Grass()

running = True
stop = False

# game main loop code
while running:
    handle_events()

    if stop is False:
        for boy in team:
            boy.update()
        for ball21 in ball21s:
            ball21.update()
        for ball41 in ball41s:
            ball41.update()

    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for ball21 in ball21s:
        ball21.draw()
    for ball41 in ball41s:
        ball41.draw()
    update_canvas()

    delay(0.05)


# finalization code
close_canvas()

from pico2d import *
import game_framework

class shooter:
    image = load_image('Shooter\\Shooter atl.png')

    def __init__(self):
        self.x = 0

    def update(self):
        self.x += 8 * game_framework.frame_time
        pass

    def draw(self):
        self.image.draw(0 - self.x,300,4000,800)

import game_framework
import main_state
from pico2d import *


name = "PauseState"
image = None
logo_time = 0.0

clicker = 0


def enter():
    global image
    image = load_image('pause.png')


def exit():
    global image
    del(image)


def update():
    global clicker
    clicker = (clicker + 1) % 200


def draw():
    global image
    global clicker
    clear_canvas()
    main_state.grass.draw()
    main_state.boy.draw()
    if (clicker < 100):
        image.draw(400, 300)
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.change_state(main_state)
    pass


def pause(): pass


def resume(): pass



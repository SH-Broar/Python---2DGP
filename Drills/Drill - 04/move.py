from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

x = 0
frame = 0
dir = 0

while (1):
    clear_canvas()
    grass.draw_now(400,30)
    if dir is 0:
        character.clip_draw(frame * 100,100,100,100, x, 90)
        update_canvas()
        frame = (frame + 1) % 8
        x += 12 + 2*abs(4-frame)
    elif dir is 1:
        character.clip_draw(frame * 100, 0, 100, 100, x, 90)
        update_canvas()
        frame = (frame + 1) % 8
        x -= 12 + 2*abs(4-frame)


    if x > 780:
        dir = 1
    elif x < 20:
        dir = 0
    delay(0.08)
    get_events()

close_canvas()


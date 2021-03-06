from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 600, 600

running = True
mx, my = KPU_WIDTH // 2, KPU_HEIGHT // 2
x, y = 10, 10
Mouse_clicked_x, Mouse_clicked_y = 10, 10
frame = 0


def handle_events():
    global running
    global mx, my, Mouse_clicked_x, Mouse_clicked_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            mx, my = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            Mouse_clicked_x, Mouse_clicked_y = mx - 25, my + 26
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def character_move():
    global Mouse_clicked_x, Mouse_clicked_y, x, y
    if Mouse_clicked_x != x:
        if Mouse_clicked_y != y:
            x += (Mouse_clicked_x - x) / 10
            y += (Mouse_clicked_y - y) / 10


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
mouse = load_image('hand_arrow.png')


while running:
    clear_canvas()
    hide_cursor()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    mouse.draw(mx, my)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8

    delay(0.02)
    handle_events()
    character_move()

close_canvas()





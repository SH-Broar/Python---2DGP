from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 600, 600

running = True
mx, my = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
pFrame = 0

flip = 0


def draw_point(p):
    global frame
    global flip
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    frame = (frame + 3) % 8

    if (flip == 0):
        character.clip_draw(frame * 100, 100 * 1, 100, 100, p[0], p[1])
    else:
        character.clip_draw(frame * 100, 100 * 0, 100, 100, p[0], p[1])

    update_canvas()
    delay(0.02)


def draw_line_2_points(p1, p2):
    global flip
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]

    if (x1 > x2):
        flip = 1
    else:
        flip = 0

    for i in range(0, 100 + 1, 2):
        t = i / 100
        x = (1 - t) * p1[0] + t * p2[0]
        y = (1 - t) * p1[1] + t * p2[1]
        draw_point((x, y))

    draw_point(p2)


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

size = 20
points = [(random.randint(0, 600), random.randint(0, 600)) for i in range(size)]

while running:
    clear_canvas()
    draw_line_2_points(points[pFrame - 1], points[pFrame])
    pFrame = (pFrame + 1) % 20

close_canvas()





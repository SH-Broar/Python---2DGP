from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 600, 600

running = True
mx, my = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
pFrame = 0

flip = 0


def draw_point(p):
    pass


def draw_line_2_points(p1, p2):
    global flip
    pass


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

size = 10
points = [(random.randint(-500, 500), random.randint(-350, 350)) for i in range(size)]

while running:
    clear_canvas()

    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    frame = (frame + 3) % 8
    character.clip_draw(frame * 100, 100 * 1, 100, 100, 300, 300)

    update_canvas()
    delay(0.02)
    draw_line_2_points(points[frame-1], points[frame])
    frame = (frame+1) % 10

close_canvas()





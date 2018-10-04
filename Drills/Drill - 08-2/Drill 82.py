from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 600, 600

running = True
mx, my = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
pFrame = 0

pre = [0,0]
flip = 0


def draw_point(p):
    global frame
    global flip
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    frame = (frame + 3) % 8

    update_canvas()
    delay(0.02)


def draw_curve_5_points(p1, p2, p3, p4, p5):
    pass


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

size = 10
points = [(random.randint(0, 600), random.randint(0, 600)) for i in range(size)]


while running:
    clear_canvas()
    draw_curve_5_points(points[pFrame-4], points[pFrame-3], points[pFrame-2], points[pFrame-1], points[pFrame])
    pFrame = (pFrame+3) % 10

close_canvas()





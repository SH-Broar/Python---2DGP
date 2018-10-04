from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 600, 600

running = True
mx, my = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
pFrame = 0

pre = [0,0]
flip = 0

stamp = -1

def draw_stamp():
    global stamp
    stamp = stamp + 8 % 8
    for i in range(-3, stamp-3):
        character.clip_draw(100, 100 * 1, 100, 100, points[i][0], points[i][1])
    pass

def draw_point(p):
    global frame
    global flip
    global points
    global stamp
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    frame = (frame + 3) % 8
    if (flip == 0):
        character.clip_draw(frame * 100, 100 * 1, 100, 100, p[0], p[1])
    else:
        character.clip_draw(frame * 100, 100 * 0, 100, 100, p[0], p[1])
    draw_stamp()
    update_canvas()
    delay(0.02)


def draw_curve_5_points(p1, p2, p3, p4, p5):
    global pre
    global flip
    global stamp
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]

    stamp = stamp + 1
    if (x1 > x2):
        flip = 1
    else:
        flip = 0
    # draw p1-p2
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p5[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p1[0] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p2[0] + (t ** 3 - t ** 2) * p3[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p5[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p1[1] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p2[1] + (t ** 3 - t ** 2) * p3[1]) / 2
        draw_point((x, y))
    draw_point(p2)

    stamp = stamp + 1

    x1, y1 = p2[0], p2[1]
    x2, y2 = p3[0], p3[1]

    if (x1 > x2):
        flip = 1
    else:
        flip = 0
    # draw p2-p3
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p1[0] + (3*t**3 - 5*t**2 + 2)*p2[0] + (-3*t**3 + 4*t**2 + t)*p3[0] + (t**3 - t**2)*p4[0])/2
        y = ((-t**3 + 2*t**2 - t)*p1[1] + (3*t**3 - 5*t**2 + 2)*p2[1] + (-3*t**3 + 4*t**2 + t)*p3[1] + (t**3 - t**2)*p4[1])/2
        draw_point((x, y))
    draw_point(p3)

    stamp = stamp + 1
    x1, y1 = p3[0], p3[1]
    x2, y2 = p4[0], p4[1]

    if (x1 > x2):
        flip = 1
    else:
        flip = 0
    # draw p3-p4
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p2[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p3[0] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p4[0] + (t ** 3 - t ** 2) * p5[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p2[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p3[1] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p4[1] + (t ** 3 - t ** 2) * p5[1]) / 2
        draw_point((x, y))
    draw_point(p4)


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





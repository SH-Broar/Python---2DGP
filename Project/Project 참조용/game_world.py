
# layer 0: Background Objects
# layer 1: Player
# layer 2: tiles
# layer 3: bullets
objects = [[],[],[],[]]


def add_object(o, layer):
    objects[layer].append(o)


def remove_object(o):
    for i in range(len(objects)):
        if o in objects[i]:
            objects[i].remove(o)
            del o


def remove_object_by_line(num):
    for i in objects[num][::-1]:
        objects[num].remove(i)
        del i


def clear():
    for o in all_objects():
        del o
    objects.clear()


def all_objects():
    for i in range(len(objects)):
        for o in objects[i]:
            yield o


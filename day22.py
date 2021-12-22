import copy
from collections import defaultdict, Counter
import numpy as np

lines = open("day22").read().split('\n')

commands = []
for line in lines:
    command = []
    if line.split(' ')[0] == 'on':
        command.append(True)
    else:
        command.append(False)

    _, line = line.split('x=')
    x1, line = line.split('..', 1)
    x2, line = line.split(',y=')
    y1, line = line.split('..', 1)
    y2, line = line.split(',z=')
    z1, z2 = line.split('..')

    x1,x2,y1,y2,z1,z2 = int(x1), int(x2), int(y1), int(y2), int(z1), int(z2)
    command.append(((min(x1,x2), max(x1,x2)), (min(y1,y2), max(y1,y2)), (min(z1,z2), max(z1,z2))))
    commands.append(command)


def overlap(cube1, cube2):
    xrange1, yrange1, zrange1 = cube1
    xrange2, yrange2, zrange2 = cube2

    xmin1, xmax1 = xrange1; ymin1, ymax1 = yrange1; zmin1, zmax1 = zrange1
    xmin2, xmax2 = xrange2; ymin2, ymax2 = yrange2; zmin2, zmax2 = zrange2

    xmin,xmax = max(xmin1, xmin2), min(xmax1, xmax2)
    ymin,ymax = max(ymin1, ymin2), min(ymax1, ymax2)
    zmin,zmax = max(zmin1, zmin2), min(zmax1, zmax2)

    if xmin <= xmax and ymin <= ymax and zmin <= zmax:
        return ((xmin, xmax), (ymin,ymax), (zmin,zmax))
    else:
        return ()


def size(cube):
    xrange, yrange, zrange = cube
    return (abs(xrange[1]-xrange[0])+1) * (abs(yrange[1]-yrange[0])+1) * (abs(zrange[1]-zrange[0])+1)


def day22_1():
    reactors = np.zeros((101, 101, 101))
    for command in commands:
        fill_value = command[0]
        x_range, y_range, z_range = command[1]
        x_range = (50+max(-50, x_range[0]), 50+min(50, x_range[1]))
        y_range = (50+max(-50, y_range[0]), 50+min(50, y_range[1]))
        z_range = (50+max(-50, z_range[0]), 50+min(50, z_range[1]))
        if x_range[0] > x_range[1] or y_range[0] > y_range[1] or z_range[0] > z_range[1]:
            continue
        reactors[x_range[0]:x_range[1]+1, y_range[0]:y_range[1]+1, z_range[0]:z_range[1]+1] = fill_value

    print(np.sum(reactors))


def day22_2():
    cubes = defaultdict(int)
    for i in range(len(commands)):
        command1 = commands[i]
        fill1, cube1 = command1
        new_cubes = copy.deepcopy(cubes)
        for cube2, value in cubes.items():
            overlapping = overlap(cube1, cube2)
            if len(overlapping) > 0:
                new_cubes[overlapping] -= value
        cubes = new_cubes
        if fill1:
            cubes[cube1] += 1

    on_size = 0
    for cube, fill in cubes.items():
        on_size += fill * size(cube)
    print(on_size)


day22_1()

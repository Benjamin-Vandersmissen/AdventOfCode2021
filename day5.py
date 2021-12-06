f = open("day5")
lines = f.read().split('\n')

import numpy as np

grid = np.zeros((1000, 1000))

def day5_1():
    for line in lines:
        point1, _, point2 = line.split(' ')
        x1, y1 = point1.split(',')
        x2, y2 = point2.split(',')
        x1,y1,x2,y2 = int(x1), int(y1), int(x2), int(y2)
        if x1 != x2 and y1 != y2:
            continue

        else:
            x_range = list(range(min(x1, x2), max(x1,x2)+1))
            y_range = list(range(min(y1, y2), max(y1,y2)+1))
            if len(x_range) > len(y_range):
                y_range = [y1] * len(x_range)
            elif len(y_range) < len(x_range):
                x_range = [x1] * len(y_range)

            for x,y in zip(x_range, y_range):
                grid[x, y] += 1


def day5_2():
    for line in lines:
        point1, _, point2 = line.split(' ')
        x1, y1 = point1.split(',')
        x2, y2 = point2.split(',')
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        x_dir = np.sign(x2-x1) if np.sign(x2-x1) != 0 else 1
        y_dir = np.sign(y2-y1) if np.sign(y2-y1) != 0 else 1
        x_range = list(range(x1, x2+x_dir, x_dir))
        y_range = list(range(y1, y2+y_dir, y_dir))
        if len(x_range) > len(y_range):
            y_range = [y1] * len(x_range)
        elif len(y_range) > len(x_range):
            x_range = [x1] * len(y_range)
        for x, y in zip(x_range, y_range):
            grid[x, y] += 1

day5_2()
print(np.sum(grid >= 2))

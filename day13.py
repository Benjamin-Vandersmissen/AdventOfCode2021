import numpy as np
f = open("day13")
lines = f.read().split('\n')

line = lines.pop(0)
dots = []
width = 0
height = 0
while line != '':
    x, y = line.split(',')
    x,y = int(x), int(y)
    width = max(width, x)
    height = max(height, y)
    dots.append((x, y))
    line = lines.pop(0)
paper = np.zeros((width+1, height+1))
for dot in dots:
    paper[dot[0], dot[1]] = 1


def fold(paper, instruction):
    if 'along x=' in instruction:
        _, x = instruction.split('along x=')
        x = int(x)
        first_half = paper[:x, :]
        second_half = np.flip(paper[x + 1:, :], axis=0)
        if second_half.shape[0] != first_half.shape[0]:  # No exact fit, add extra 0-filled row
            second_half = np.vstack((np.zeros((1, second_half.shape[1])), second_half))
        return np.logical_or(first_half, second_half)

    if 'along y=' in instruction:
        _, y = instruction.split('along y=')
        y = int(y)
        first_half = paper[:, :y]
        second_half = np.flip(paper[:, y + 1:], axis=1)
        if second_half.shape[1] != first_half.shape[1]:  # No exact fit, add extra 0-filled column
            second_half = np.hstack((np.zeros((second_half.shape[0], 1)), second_half))
        return np.logical_or(first_half, second_half)


def day13_1():
    global paper
    paper = fold(paper, lines[0])
    print(np.sum(paper))


def day13_2():
    global paper
    for line in lines:
        paper = fold(paper, line)

    paper = paper.astype(int)
    paper = np.transpose(paper, (1, 0))
    for i in range(paper.shape[0]):
        row = ""
        for j in range(paper.shape[1]):
            row += "\u25A0" if paper[i, j] else " "
        print(row)

day13_2()

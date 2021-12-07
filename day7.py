import numpy as np
f = open("day7")
positions = np.array([int(pos) for pos in f.read().split(',')])


def day7_1():
    median = np.median(positions)
    print(np.abs(positions-median).sum())


def day7_2():
    values = [0]
    for i in range(1, 2000):
        values.append(values[i-1]+i)
    values = np.array(values)
    mean = np.round(np.mean(positions)).astype(int)-1
    differences = np.abs(positions-mean)
    print(values[differences].sum())

day7_2()
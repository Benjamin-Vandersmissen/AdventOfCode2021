import numpy as np

f = open("day11")
lines = f.read().split('\n')
octopi = []
for line in lines:
    row = []
    for c in line:
        row.append(int(c))
    octopi.append(row)

octopi = np.array(octopi)


def day11_1():
    octopi = []
    count = 0
    for line in lines:
        row = []
        for c in line:
            row.append(int(c))
        octopi.append(row)

    octopi = np.array(octopi)
    for step in range(100):
        octopi += np.ones_like(octopi)
        to_add = np.zeros_like(octopi)
        changed = np.zeros_like(octopi)
        changed_old = np.ones_like(octopi)
        while True:
            bla = octopi + to_add
            if (changed == changed_old).all():
                break
            changed_old = changed.copy()
            for i in range(octopi.shape[0]):
                for j in range(octopi.shape[1]):
                    if changed[i,j]:
                        continue
                    if bla[i,j] > 9:
                        changed[i,j] = 1
                        if i > 0:
                            to_add[i-1, j] += 1
                        if j > 0:
                            to_add[i, j-1] += 1
                        if i > 0 and j > 0:
                            to_add[i-1, j-1] += 1
                        if i > 0 and j < octopi.shape[1]-1:
                            to_add[i-1,j+1] += 1
                        if i < octopi.shape[0]-1 and j > 0:
                            to_add[i+1,j-1] += 1
                        if i < octopi.shape[0]-1 and j < octopi.shape[1]-1:
                            to_add[i+1,j+1] += 1
                        if i < octopi.shape[0]-1:
                            to_add[i+1,j] += 1
                        if j < octopi.shape[1]-1:
                            to_add[i,j+1] += 1
        octopi += to_add
        count += np.sum(octopi > 9)
        octopi[octopi > 9] = 0
        print(count)


def day11_2():
    octopi = []
    timestep = 0
    for line in lines:
        row = []
        for c in line:
            row.append(int(c))
        octopi.append(row)

    octopi = np.array(octopi)
    while True:
        octopi += np.ones_like(octopi)
        to_add = np.zeros_like(octopi)
        changed = np.zeros_like(octopi)
        changed_old = np.ones_like(octopi)
        while True:
            bla = octopi + to_add
            if (changed == changed_old).all():
                break
            changed_old = changed.copy()
            for i in range(octopi.shape[0]):
                for j in range(octopi.shape[1]):
                    if changed[i,j]:
                        continue
                    if bla[i,j] > 9:
                        changed[i,j] = 1
                        if i > 0:
                            to_add[i-1, j] += 1
                        if j > 0:
                            to_add[i, j-1] += 1
                        if i > 0 and j > 0:
                            to_add[i-1, j-1] += 1
                        if i > 0 and j < octopi.shape[1]-1:
                            to_add[i-1,j+1] += 1
                        if i < octopi.shape[0]-1 and j > 0:
                            to_add[i+1,j-1] += 1
                        if i < octopi.shape[0]-1 and j < octopi.shape[1]-1:
                            to_add[i+1,j+1] += 1
                        if i < octopi.shape[0]-1:
                            to_add[i+1,j] += 1
                        if j < octopi.shape[1]-1:
                            to_add[i,j+1] += 1
        octopi += to_add
        octopi[octopi > 9] = 0
        timestep += 1
        if (octopi == np.zeros_like(octopi)).all():
            print(timestep)
            return

day11_2()
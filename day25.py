import numpy as np

lines = open("day25").read().split('\n')

mapping = {'>':1, 'v':-1, '.':0}

array = []
for line in lines:
    array.append([mapping[obj] for obj in line])

array = np.array(array)

moved = True
nr_moved = 0
while moved:
    moved = False
    new_array = np.zeros_like(array)
    for i in range(array.shape[1]):
        next_idx = (i+1)%array.shape[1]
        prev_idx = (i-1)%array.shape[1]
        cur_col = array[:, i]
        next_col = array[:, next_idx]
        prev_col = array[:, prev_idx]

        cond1 = np.logical_and(next_col == 0, cur_col == 1)
        new_col = np.where(cond1, 0, cur_col)
        cond2 = np.logical_and(cur_col == 0, prev_col == 1)
        new_col = np.where(cond2, prev_col, new_col)

        new_array[:, i] = new_col

    moved = not (array == new_array).all()
    array = new_array
    new_array = np.zeros_like(array)
    for i in range(array.shape[0]):
        next_idx = (i + 1) % array.shape[0]
        prev_idx = (i - 1) % array.shape[0]
        cur_row = array[i]
        next_row = array[next_idx]
        prev_row = array[prev_idx]

        cond1 = np.logical_and(next_row == 0, cur_row == -1)
        new_row = np.where(cond1, 0, cur_row)
        cond2 = np.logical_and(cur_row == 0, prev_row == -1)
        new_row = np.where(cond2, prev_row, new_row)

        new_array[i] = new_row

    moved = moved or not (array == new_array).all()
    array = new_array
    nr_moved += 1
print(nr_moved)

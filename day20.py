import numpy as np

lines = open('day20').read().split('\n')

mapping = np.array([0 if c == '.' else 1 for c in lines[0]])
lines = lines[2:]

array = []
for line in lines:
    temp = [0 if c == '.' else 1 for c in line]
    array.append(temp)
array = np.array(array)


def position_to_value(arr, position):
    row,col = position

    bit_str = ""
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            bit_str += str(arr[i, j])
    return int(bit_str, 2)


def enhance(arr, nr_it=2):
    fill_value = 0
    for i in range(nr_it):
        if i >0:
            fill_value = mapping[int(9*str(fill_value), 2)]
        top_down = np.full((2, arr.shape[1]), fill_value, dtype=int)
        arr = np.vstack((top_down, arr, top_down))
        left_right = np.full((arr.shape[0], 2), fill_value, dtype=int)
        arr = np.hstack((left_right, arr, left_right))

        out = np.zeros((arr.shape[0]-2, arr.shape[1]-2), dtype=int)
        for row in range(1, arr.shape[0]-1):
            for col in range(1, arr.shape[1]-1):
                out[row-1,col-1] = mapping[position_to_value(arr, (row,col))]
        arr = out
    print(arr.sum())


def day20_1():
    enhance(array, 2)


def day20_2():
    enhance(array, 50)


day20_2()

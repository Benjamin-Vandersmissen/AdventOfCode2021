import numpy as np
import pandas as pd
from skimage.measure import label, regionprops, regionprops_table
f = open("day9")

data = [line for line in f.read().split('\n')]
new_data = []
for line in data:
    new_data.append([int(i) for i in line])
new_data = np.array(new_data)


def day9_1():
    top_matrix = np.vstack((np.full((1, new_data.shape[1]), 10), new_data[:-1, :]))
    bottom_matrix = np.vstack((new_data[1:, :], np.full((1, new_data.shape[1]), 10)))
    left_matrix = np.hstack((np.full((new_data.shape[0], 1), 10), new_data[:, :-1]))
    right_matrix = np.hstack((new_data[:, 1:], np.full((new_data.shape[0], 1), 10)))

    low_points = np.logical_and(np.logical_and(new_data < top_matrix, new_data < bottom_matrix), np.logical_and(new_data < right_matrix, new_data < left_matrix))
    risk = np.sum(new_data[low_points] + 1)
    print(risk)


def day9_2():
    modified_data = new_data < 9
    label_im = label(modified_data, connectivity=1)
    areas = pd.DataFrame(regionprops_table(label_im, modified_data, ['area'])).sort_values('area', ascending=False)[:3]['area']
    print(areas.iloc[0]*areas.iloc[1]*areas.iloc[2])
day9_2()
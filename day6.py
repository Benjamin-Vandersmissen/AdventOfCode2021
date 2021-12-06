import numpy as np

f = open("day6")
fishes = np.array([int(fish) for fish in f.read().split(',')])

day_mapping = {}


def calculate_new_fishes(fish, days, mapping):
    initial_days = days
    if (fish, days) in mapping:
        return mapping[(fish, days)]
    n_fishes = 1
    days -= fish + 1
    while days >= 0:
        if (0, days) in mapping:
            new_fishes = mapping[(0, days)]
        else:
            new_fishes = calculate_new_fishes(8, days, mapping)
            mapping[(0, days)] = new_fishes
        n_fishes += new_fishes
        fish = 6
        days -= fish + 1
    mapping[(fish, initial_days)] = n_fishes
    return n_fishes

mapping = [calculate_new_fishes(i, 256, day_mapping) for i in range(6)]

result = sum([np.sum(fishes == i) * mapping[i] for i in range(6)])
print(result)

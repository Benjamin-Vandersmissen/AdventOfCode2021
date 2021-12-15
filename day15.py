import numpy as np

f = open("day15")
lines = f.read().split('\n')

array = []
for line in lines:
    array.append([int(value) for value in line])

array = np.asarray(array)

minimum_score = 753
minimum_path = []

estimated_costs = -1 * np.ones_like(array)

def taxicab(start, end):
    return abs(end[0] - start[0]) + abs(end[1] - start[1])

def estimate_cost(position, base_cost):
    return base_cost + array[position[0], position[1]]

def dijkstra(start, end):
    cost_array = 20000 * np.ones_like(array,dtype=int)
    cost_array[0,0] = 0

    unvisited = [start]
    visited = np.zeros_like(cost_array)

    while unvisited:
        node = unvisited.pop(0)
        if node[0] < array.shape[0] - 1 and not visited[node[0] + 1, node[1]]:
            pos = (node[0] + 1, node[1])
            cost_array[pos] = min(cost_array[pos], estimate_cost(pos, cost_array[node]))
            unvisited.append(pos)

        if node[1] < array.shape[1] - 1 and not visited[node[0], node[1] + 1]:
            pos = (node[0], node[1] + 1)
            cost_array[pos] = min(cost_array[pos], estimate_cost(pos, cost_array[node]))
            unvisited.append(pos)

        if node[0] > 0 and not visited[node[0] - 1, node[1]]:
            pos = (node[0] - 1, node[1])
            cost_array[pos] = min(cost_array[pos], estimate_cost(pos, cost_array[node]))
            unvisited.append(pos)

        if node[1] > 0 and not visited[node[0], node[1] - 1]:
            pos = (node[0], node[1] - 1)
            cost_array[pos] = min(cost_array[pos], estimate_cost(pos, cost_array[node]))
            unvisited.append(pos)

        unvisited = list(set(unvisited))
        unvisited.sort(key=lambda x: cost_array[x[0], x[1]] + taxicab(x, end))
        visited[node[0], node[1]] = 1
    print(cost_array[end])

def day15_1():
    dijkstra((0,0), (-1,-1))


def day15_2():
    global array
    new_array = np.zeros((5*array.shape[0], 5*array.shape[1]))
    for i in range(5):
        for j in range(5):
            extra_risk = taxicab((i,j), (0,0))

            extra_risk = extra_risk % 9
            temp = array + extra_risk
            temp[temp > 9] -= 9

            new_array[i*array.shape[0]:(i+1)*array.shape[0], j*array.shape[1]:(j+1)*array.shape[1]] = temp
    array = new_array
    dijkstra((0,0), (array.shape[0]-1,array.shape[1]-1))

day15_2()
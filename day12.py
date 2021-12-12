f = open("day12")
lines = f.read().split('\n')

connections = {}
for line in lines:
    s, e = line.split('-')
    if s not in connections:
        connections[s] = [e]
    else:
        connections[s].append(e)
    if e not in connections:
        connections[e] = [s]
    else:
        connections[e].append(s)

all_paths = set()


def find_path_recursive(current_path, allow_double_small=False, double_small=False):
    global all_paths
    if current_path[-1] not in connections:
        return
    if current_path[-1] == 'end':
        all_paths.add(current_path)
        return
    for node in connections[current_path[-1]]:
        if node.islower() and node in current_path:
            if allow_double_small and not double_small and node != 'start':
                find_path_recursive((*current_path, node), allow_double_small, True)
            else:
                continue
        else:
            find_path_recursive((*current_path,node), allow_double_small, double_small)


def day12_1():
    global all_paths
    start_path = ('start',)
    find_path_recursive(start_path)
    print(len(all_paths))


def day12_2():
    global all_paths
    start_path = ('start',)
    find_path_recursive(start_path, allow_double_small=True)
    print(len(all_paths))


day12_2()
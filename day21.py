from itertools import product

lines = open("day21").read().split('\n')

pos_1 = int(lines[0].split(': ')[1])
pos_2 = int(lines[1].split(': ')[1])


score_1 = 0
score_2 = 0

deterministic_die = 1
nr_rolled = 0

def deterministic():
    global deterministic_die, nr_rolled
    out = 0
    for i in range(3):
        nr_rolled += 1
        out += deterministic_die
        deterministic_die = deterministic_die % 100 + 1
    return out


def day21_1():
    global score_1, score_2, pos_1, pos_2
    while True:
        throw = deterministic()
        nr_steps = throw % 10
        pos_1 = pos_1 + nr_steps
        if pos_1 > 10:
            pos_1 -= 10
        score_1 += pos_1

        if score_1 >= 1000:
            break

        nr_steps = deterministic() % 10
        pos_2 = pos_2 + nr_steps
        if pos_2 > 10:
            pos_2 -= 10
        score_2 += pos_2

        if score_2 >= 1000:
            break

    print(min(nr_rolled * score_1, nr_rolled * score_2))


cache = {}

def recursive(pos_1, pos_2, score_1, score_2, move):
    win1 = 0
    win2 = 0

    if (pos_1, pos_2, score_1, score_2, move) in cache:
        return cache[(pos_1, pos_2, score_1, score_2, move)]

    if score_1 >= 21:
        win1 += 1
        return win1, win2

    if score_2 >= 21:
        win2 += 1
        return win1, win2

    for outcome in product((1,2,3), repeat=3):
        to_move = sum(outcome)
        if move:
                new_pos = pos_1
                new_pos += to_move
                if new_pos > 10:
                    new_pos -= 10
                new_win1, new_win2 = recursive(new_pos, pos_2, score_1 + new_pos, score_2, not move)
        else:
                new_pos = pos_2
                new_pos += to_move
                if new_pos > 10:
                    new_pos -= 10
                new_win1, new_win2 = recursive(pos_1, new_pos, score_1, score_2 + new_pos, not move)

        win1, win2 = win1 + new_win1, win2 + new_win2

    cache[(pos_1, pos_2, score_1, score_2, move)] = win1, win2
    return win1, win2


def day21_2():
    global pos_1, pos_2
    recursive(pos_1, pos_2, 0, 0, True)
    print(max(cache[(pos_1, pos_2, 0, 0, True)]))


day21_2()

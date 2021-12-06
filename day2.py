f = open("day2")
lines = f.read().split('\n')


def day2_1():
    x_pos = 0
    y_pos = 0

    for line in lines:
        direction, value = line.split(' ')
        value = int(value)

        if direction == 'down':
            y_pos += value
        if direction == 'up':
            y_pos -= value
        if direction == 'forward':
            x_pos += value
        if direction == 'backward':
            x_pos -= value

    return x_pos, y_pos


def day2_2():
    x_pos = 0
    y_pos = 0
    aim = 0

    for line in lines:
        direction, value = line.split(' ')
        value = int(value)

        if direction == 'down':
            aim += value
        if direction == 'up':
            aim -= value
        if direction == 'forward':
            x_pos += value
            y_pos += aim * value
        if direction == 'backward':
            x_pos -= value
            y_pos -= aim * value

    return x_pos, y_pos


x_pos, y_pos = day2_2()
print(x_pos*y_pos)

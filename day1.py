f = open("day1")
lines = f.read().split('\n')
lines = [int(line) for line in lines]

def day1_1():
    count_increasing = 0
    for i in range(1,len(lines)):
        if lines[i] > lines[i-1]:
            count_increasing += 1

    print(count_increasing)

def day1_2(window_size=3):
    count_increasing = 0
    for i in range(window_size, len(lines)):
        if sum(lines[i-window_size:i]) > sum(lines[i-window_size-1:i-1]):
            count_increasing += 1
    print(count_increasing)

day1_2()
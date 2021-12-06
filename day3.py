f = open("day3")
lines = f.read().split('\n')


def day3_1():
    booleans = []

    for line in lines:
        for i in range(len(line)):
            if i >= len(booleans):
                booleans.append(int(line[i]))
            else:
                booleans[i] += int(line[i])

    for i in range(len(booleans)):
        booleans[i] = int(booleans[i] > len(lines) // 2)

    print(booleans)


def day3_2():
    most_frequent_lines = lines
    for i in range(len(most_frequent_lines[0])):
        boolean = 0
        for line in most_frequent_lines:
            boolean += 2*int(line[i]) - 1
        most_frequent_bit = int(boolean >= 0)
        most_frequent_lines = [line for line in most_frequent_lines if line[i] == str(most_frequent_bit)]
        if len(most_frequent_lines) == 1:
            print("MOST")
            print(most_frequent_lines)
            break

    least_frequent_lines = lines
    for i in range(len(least_frequent_lines[0])):
        boolean = 0
        for line in least_frequent_lines:
            boolean += 2*int(line[i])-1
        least_frequent_bit = int(boolean < 0)
        least_frequent_lines = [line for line in least_frequent_lines if line[i] == str(least_frequent_bit)]
        if len(least_frequent_lines) == 1:
            print("LEAST")
            print(least_frequent_lines)
            break

day3_2()
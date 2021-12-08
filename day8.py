f = open("day8")
lines = f.read().split('\n')

unique_patterns = [line.split(' | ')[0] for line in lines]
outputs = [line.split(' | ')[1] for line in lines]

unique_patterns = [line.split(' ') for line in unique_patterns]
outputs = [line.split(' ') for line in outputs]


def contains(a, b):
    cont = True
    for i in range(len(b)):
        cont = cont and b[i] in a
    return cont


def day8_1():
    total_recognised = 0
    for outp in outputs:
        for number in outp:
            if len(number) in [2,3,4,7]:
                total_recognised += 1
    print(total_recognised)


def day8_2():
    total_sum = 0
    for i in range(len(unique_patterns)):
        patterns = unique_patterns[i]
        number_mapping = {}
        for pattern in patterns:
            if len(pattern) == 2:
                number_mapping[1] = pattern
            if len(pattern) == 3:
                number_mapping[7] = pattern
            if len(pattern) == 4:
                number_mapping[4] = pattern
            if len(pattern) == 7:
                number_mapping[8] = pattern

        top_segment = [segment for segment in number_mapping[7] if segment not in number_mapping[1]][0]
        number_mapping[9] = [pattern for pattern in patterns if top_segment in pattern and contains(pattern, number_mapping[4]) and len(pattern) == 6][0]
        bottom_left_segment = [segment for segment in number_mapping[8] if segment not in number_mapping[9]][0]
        number_mapping[3] = [pattern for pattern in patterns if len(pattern) == 5 and contains(pattern, number_mapping[1])][0]
        number_mapping[2] = [pattern for pattern in patterns if len(pattern) == 5 and bottom_left_segment in pattern][0]
        number_mapping[5] = [pattern for pattern in patterns if len(pattern) == 5 and pattern not in number_mapping.values()][0]
        number_mapping[6] = [pattern for pattern in patterns if len(pattern) == 6 and contains(pattern, number_mapping[5]) and pattern not in number_mapping.values()][0]
        number_mapping[0] = [pattern for pattern in patterns if pattern not in number_mapping.values()][0]

        gen_output = ''
        for output in outputs[i]:
            for key, value in number_mapping.items():
                if len(output) == len(value) and contains(output, value):
                    gen_output += str(key)
                    break
        total_sum += int(gen_output)
    print(total_sum)


day8_2()

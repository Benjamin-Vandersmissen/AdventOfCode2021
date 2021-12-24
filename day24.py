import collections
from functools import cache

instructions = open("day24").read().split('\n')

instructions_per_inp = []
temp = []
for instruction in instructions:
    if 'inp' in instruction and len(temp) > 0:
        instructions_per_inp.append(temp)
        temp = []
    temp.append(instruction)
instructions_per_inp.append(temp)
input = [1]*14


def execute(instruction, stack, inp):
    if not ' ' in instruction:
        return stack
    opcode = instruction.split(' ')[0]
    if opcode == 'inp':
        arg1 = instruction.split(' ')[1]
        stack[arg1] = inp
    else:
        _, arg1, arg2 = instruction.split(' ')
        if not arg2 in ['x', 'y', 'z', 'w']:
            arg2 = int(arg2)
        else:
            arg2 = stack[arg2]

        if opcode == 'add':
            stack[arg1] += arg2
        if opcode == 'mul':
            stack[arg1] *= arg2
        if opcode == 'div':
            stack[arg1] //= arg2
        if opcode == 'mod':
            stack[arg1] %= arg2
        if opcode == 'eql':
            stack[arg1] = int(stack[arg1] == arg2)
    return stack

@cache
def determine_inp():
    values = {0: ['']}
    for pos in range(14):
        new_values = collections.defaultdict(list)
        for previous_z, previous_in in values.items():
            possible_values = []

            for i in range(1, 10):
                stack = {'x': 0, 'y': 0, 'z': previous_z, 'w': 0}
                for instruction in instructions_per_inp[pos]:
                    stack = execute(instruction, stack, i)

                new_strs = [''.join([new_str, str(i)]) for new_str in previous_in]
                possible_values.append((stack['z'], new_strs))

            if 'div z 26' in instructions_per_inp[pos]:
                possible_values = sorted(possible_values, key=lambda x: x[0])
                new_values[possible_values[0][0]] += possible_values[0][1]
            else:
                for pair in possible_values:
                    new_values[pair[0]] += pair[1]
        values = new_values
        print("iteration {} done, found {} possible z's.".format(pos+1, len(values)))
    return sorted(values[0])


def day24_1():
    print(determine_inp()[-1])


def day24_2():
    print(determine_inp()[0])


day24_1()

day24_2()

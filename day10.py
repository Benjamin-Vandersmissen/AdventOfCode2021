f = open("day10")
lines = f.read().split('\n')


def day10_1():
    score = 0
    for line in lines:
        stack = []
        for char in line:
            if char == '(' or char == '[' or char == '{' or char == '<':
                stack.append(char)
            else:
                starting = stack.pop()
                if char == ')' and starting != '(':
                    score += 3
                    break
                elif char == ']' and starting != '[':
                    score += 57
                    break
                elif char == '}' and starting != '{':
                    score += 1197
                    break
                elif char == '>' and starting != '<':
                    score += 25137
                    break

    print(score)


def day10_2():
    scores = []
    for line in lines:
        stack = []
        corrupted = False
        for char in line:
            if char == '(' or char == '[' or char == '{' or char == '<':
                stack.append(char)
            else:
                starting = stack.pop()
                if char == ')' and starting != '(':
                    corrupted = True
                    break
                elif char == ']' and starting != '[':
                    corrupted = True
                    break
                elif char == '>' and starting != '<':
                    corrupted = True
                    break
                elif char == '}' and starting != '{':
                    corrupted = True
                    break

        if len(stack) != 0 and not corrupted:
            score = 0
            while len(stack) != 0:
                c = stack.pop()
                score = score * 5
                if c == '(':
                    score += 1
                if c == '[':
                    score += 2
                if c == '{':
                    score += 3
                if c == '<':
                    score += 4
            scores.append(score)

    scores = sorted(scores)
    print(scores[(len(scores)-1)//2])


day10_2()
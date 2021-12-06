f = open("day4")
lines = f.read().split('\n')

numbers = [int(number) for number in lines.pop(0).split(',')]

lines.pop(0)
boards = []
board = []
while len(lines) > 0:
    line = lines.pop(0)
    if line == '':
        boards.append(board)
        board = []
        continue
    board.append([int(number) for number in line.split(' ') if number != ''])
boards.append(board)

def day4_1():
    for number in numbers:
        for board in boards:
            for row in board:
                if number in row:
                    row[row.index(number)] = 0
                if sum(row) == 0:
                    print(sum([sum(row) for row in board]) * number)
                    return
            for i in range(len(board)):
                col = [row[i] for row in board]
                if sum(col) == 0:
                    print(sum([sum(row) for row in board]) * number)
                    return


def day4_2():
    global boards
    for number in numbers:
        remove_boards = []
        for j in range(len(boards)):
            board = boards[j]
            for row in board:
                if number in row:
                    row[row.index(number)] = 0
                if sum(row) == 0:
                    if len(boards) == 1:
                        print(sum([sum(row) for row in board]) * number)
                        return
                    else:
                        remove_boards.append(board)
            for i in range(len(board)):
                col = [row[i] for row in board]
                if sum(col) == 0:
                    if len(boards) == 1:
                        print(sum([sum(row) for row in board]) * number)
                        return
                    else:
                        remove_boards.append(board)

        boards = [board for board in boards if board not in remove_boards]
day4_2()
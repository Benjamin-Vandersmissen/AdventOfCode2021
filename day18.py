import copy

lines = open("day18").read().split('\n')


class Pair:
    def __init__(self, val1, val2, nest_level=0):
        self.left = val1
        self.right = val2
        self.nest_level = nest_level
        if isinstance(self.left, Pair):
            self.left.parent = self
        if isinstance(self.right, Pair):
            self.right.parent = self
        self.parent = None

    @staticmethod
    def read_from_string(string, nest_level=0):
        string = string[1:]
        if string[0] == '[':
            left, string = Pair.read_from_string(string, nest_level+1)
            _ , right = string.split(',', maxsplit=1)
        else:
            left, right = string.split(',', maxsplit=1)
            left = int(left)

        if right[0] == '[':
            right, string = Pair.read_from_string(right, nest_level+1)
        else:
            right, string = right.split(']', maxsplit=1)
            right = int(right)
        pair =  Pair(left, right, nest_level)
        if isinstance(pair.left, Pair):
            pair.left.parent = pair
        if isinstance(pair.right, Pair):
            pair.right.parent = pair
        return pair, string

    def unnested(self):
        left_unnested = self.left.unnested() if isinstance(self.left, Pair) else []
        right_unnested = self.right.unnested() if isinstance(self.right, Pair) else []
        return left_unnested + [self] + right_unnested

    @staticmethod
    def add(left, right):
        new_pair = Pair(left, right)
        for value in new_pair.unnested():
            if isinstance(value, Pair) and value != new_pair:
                value.nest_level += 1

        broken = True
        while broken:
            broken = False
            unnested = new_pair.unnested()
            for i in range(len(unnested)):  # SEARCH FOR POSSIBLE EXPLOSIONS
                unnested_pair = unnested[i]
                if unnested_pair.nest_level >= 4 and not isinstance(unnested_pair.right, Pair) and not isinstance(unnested_pair.left, Pair) :
                    first_left = unnested_pair.first_left()
                    first_right = unnested_pair.first_right()
                    if first_left != unnested_pair:
                        if isinstance(first_left.right, Pair):
                            first_left.left += unnested_pair.left
                        else:
                            first_left.right += unnested_pair.left
                    if first_right != unnested_pair:
                        if isinstance(first_right.left, Pair):
                            first_right.right += unnested_pair.right
                        else:
                            first_right.left += unnested_pair.right
                    if unnested_pair.parent.left == unnested_pair:
                        unnested_pair.parent.left = 0
                    else:
                        unnested_pair.parent.right = 0
                    broken = True
                    break
            if broken:
                continue

            for i in range(len(unnested)):  # SEARCH FOR POSSIBLE SPLITS
                unnested_pair = unnested[i]

                if isinstance(unnested_pair.left, int) and unnested_pair.left > 9:
                    unnested_pair.left = Pair(unnested_pair.left//2, (unnested_pair.left + 1)//2, unnested_pair.nest_level+1)
                    unnested_pair.left.parent = unnested_pair
                    broken = True
                    break
                if isinstance(unnested_pair.right, int) and unnested_pair.right > 9:
                    unnested_pair.right = Pair(unnested_pair.right//2, (unnested_pair.right + 1)//2, unnested_pair.nest_level+1)
                    unnested_pair.right.parent = unnested_pair
                    broken = True
                    break

        return new_pair

    def first_left(self):
        node = self
        while node.parent is not None:
            if node.parent.right == node:
                if isinstance(node.parent.left, Pair):
                    return node.parent.left.rightmost()
                else:
                    return node.parent
            node = node.parent
        return self

    def first_right(self):
        node = self
        while node.parent is not None:
            if node.parent.left == node:
                if isinstance(node.parent.right, Pair):
                    return node.parent.right.leftmost()
                else:
                    return node.parent
            node = node.parent
        return self

    def leftmost(self):
        if isinstance(self.left, Pair):
            return self.left.leftmost()
        else:
            return self

    def rightmost(self):
        if isinstance(self.right, Pair):
            return self.right.rightmost()
        else:
            return self

    def __repr__(self):
        return '[' + self.left.__repr__() + ',' + self.right.__repr__() + ']'

    def magnitude(self):
        if isinstance(self.left, Pair):
            left = self.left.magnitude()
        else:
            left = self.left
        if isinstance(self.right, Pair):
            right = self.right.magnitude()
        else:
            right = self.right
        return 3*left + 2*right


pairs = [Pair.read_from_string(line)[0] for line in lines]


def day18_1():
    total = pairs[0]
    for i in range(1, len(pairs)):
        total = Pair.add(total, pairs[i])
    print(total.magnitude())


def day18_2():
    max_magnitude = 0
    for pair1 in pairs:
        for pair2 in pairs:
            sum_pair = Pair.add(copy.deepcopy(pair1), copy.deepcopy(pair2))
            max_magnitude = max(max_magnitude, sum_pair.magnitude())
    print(max_magnitude)


day18_2()
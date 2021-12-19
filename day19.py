import itertools

lines = open("day19").read().split('\n')

scanners = []
current_scanner = []

for line in lines:
    if line[:2] == '--':
        current_scanner = []
        continue

    if line == '':
        scanners.append(current_scanner)
        continue

    x,y,z = line.split(',')
    x,y,z = int(x), int(y), int(z)
    current_scanner.append((x,y,z))
scanners.append(current_scanner)

def sin(theta):
    if theta == 0 or theta == 180:
        return 0
    if theta == 90:
        return 1
    if theta == 270:
        return -1

def cos(theta):
    if theta == 90 or theta == 270:
        return 0
    if theta == 0:
        return 1
    if theta == 180:
        return -1

def offset(point1, point2):
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    return x2-x1, y2-y1, z2-z1


def add(point1, point2):
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    return x1+x2, y1+y2, z1+z2

def rotate_around(point, rotations):
    x, y, z = point
    rx, ry, rz = rotations
    rx, ry, rz = rx % 360, ry % 360, rz % 360
    # rotate around x
    x, y, z = x, cos(rx)*y - sin(rx)*z, sin(rx)*y + cos(rx)*z

    # rotate around y
    x, y, z = cos(ry)*x+sin(ry)*z, y, -sin(ry)*x+cos(ry)*z

    # rotate around z
    x, y, z = cos(rz)*x-sin(rz)*y, sin(rz)*x+cos(rz)*y, z

    return x, y, z


rotations = [
    [0, 0, 0],
    [90, 0, 0],
    [180, 0, 0],
    [270, 0, 0],
    [0, 90, 0],
    [90, 90, 0],
    [180, 90, 0],
    [270, 90, 0],
    [0, 180, 0],
    [90, 180, 0],
    [180, 180, 0],
    [270, 180, 0],
    [0, 270, 0],
    [90, 270, 0],
    [180, 270, 0],
    [270, 270, 0],
    [0, 0, 90],
    [90, 0, 90],
    [180, 0, 90],
    [270, 0, 90],
    [0, 0, 270],
    [90, 0, 270],
    [180, 0, 270],
    [270, 0, 270]
]


def transform_to_zero_basis(transforms):
    # Stack transforms until we have a set of transforms to move all scanners to the basis of the first scanner
    transform_mapping = {0: []}
    scanner_mapping = {0: (0,0,0)}  # the location of the scanners in the basis of scanner 0
    points = set(scanners[0])
    while len(scanner_mapping) != len(scanners):
        for i,j in transforms.keys():
            rot, diff = transforms[i, j]
            if i in transform_mapping and j not in transform_mapping:
                new_scanner = [add(rotate_around(point, rot), diff) for point in scanners[j]]
                scanner_orig = add(rotate_around((0, 0, 0), rot), diff)
                for transf in transform_mapping[i]:
                    new_rot, new_diff = transf
                    new_scanner = [add(rotate_around(point, new_rot), new_diff) for point in new_scanner]
                    scanner_orig = add(rotate_around(scanner_orig, new_rot), new_diff)

                transform_mapping[j] = [(rot, diff)] + transform_mapping[i]
                points.update(set(new_scanner))
                scanner_mapping[j] = scanner_orig
    return points, scanner_mapping


transforms = dict()
for s1 in range(len(scanners)):
    scanner1 = scanners[s1]
    for s2 in range(0, len(scanners)):
        if s1 == s2:
            continue
        scanner2 = scanners[s2]
        done = False
        for rot in rotations:
            rot_scanner2 = [rotate_around(p, rot) for p in scanner2]
            dist_map = dict()
            for i, j in itertools.product(range(len(scanner1)), range(len(rot_scanner2))):
                p1 = scanner1[i]
                p2 = scanner2[j]
                rot_p2 = rot_scanner2[j]
                dist = offset(rot_p2, p1)
                if dist in dist_map:
                    dist_map[dist] += [(p1, p2)]
                else:
                    dist_map[dist] = [(p1,p2)]
            for key in dist_map:
                if len(dist_map[key]) >= 12:
                    value = dist_map[key]
                    done = True
                    transforms[(s1, s2)] = (rot, key)
            if done:
                break
points, scanner_map = transform_to_zero_basis(transforms)


def day19_1():
    print(len(points))


def day19_2():
    max_dist = 0
    for scanner in scanner_map.values():
        for scanner2 in scanner_map.values():
            x1,y1,z1 = scanner
            x2,y2,z2 = scanner2
            dist = abs(x2-x1) + abs(y2-y1) + abs(z2-z1)
            max_dist = max(dist, max_dist)
    print(max_dist)


day19_2()
line = open("day17").read()

_, x_range = line.split('x=')
x_range, _ = x_range.split(',')
xmin, xmax = [int(val) for val in x_range.split('..')]
_, y_range = line.split('y=')
ymin, ymax = [int(val) for val in y_range.split('..')]

x, y = 0, 0
x_vel, y_vel = 6, 9

# xmin, xmax, ymin, ymax = 20, 30, -10, -5


x_temp = 0
for i in range(100):
    x_temp += i
    if x_temp > xmax:
        x_vel = i-1
        print("x vel = {}".format(x_vel))
        break

def day17_1():
    global x_vel
    for y_vel in range(x_vel, 500):
        y_vel_ = y_vel
        x_vel_ = x_vel
        y_top = 0
        x, y = 0, 0
        while True:
            x, y = x + x_vel_, y + y_vel_
            if x_vel_ > 0:
                x_vel_ -= 1
            elif x_vel_ < 0:
                x_vel_ += 1
            elif y < ymin:
                break
            y_vel_ -= 1
            if y_vel_ == 0:
                y_top = y
            if xmax >= x >= xmin and ymax >= y >= ymin:
                print("found : {}, {}".format(x_vel, y_vel))
                print("Max y : {}".format(y_top))
                break

def day17_2():
    global x_vel
    speeds = []
    for x_vel in range(x_vel, xmax+1):
        for y_vel in range(ymin, 500):
            x, y = 0, 0
            x_vel_, y_vel_ = x_vel, y_vel
            while True:
                x, y = x + x_vel_, y + y_vel_
                if x_vel_ > 0:
                    x_vel_ -= 1
                elif x_vel_ < 0:
                    x_vel_ += 1
                elif x < xmin or x > xmax:
                    break
                if y < ymin:
                    break
                y_vel_ -= 1
                if xmax >= x >= xmin and ymax >= y >= ymin:
                    print("found : {}, {}".format(x_vel, y_vel))
                    speeds.append((x_vel, y_vel))
                    break
    print(len(speeds))

day17_2()
import math


def dist_btw_points(a, b):
    return math.sqrt((int(a[0]) - int(b[0])) ** 2 + (int(a[1]) - int(b[1])) ** 2)


def figure_perimetr(input):
    values = input[1:].split('#')
    for i in range(len(values)):
        values[i] = values[i][2:].split(':')
    values.append(values[0])
    values[2], values[3] = values[3], values[2]
    perimeter = 0
    for j in range(1, len(values)):
        perimeter += dist_btw_points(values[j], values[j - 1])
    return round(perimeter, 14)


if __name__ == '__main__':
    test1 = "#LB1:1#RB4:1#LT1:3#RT4:3"
    print(figure_perimetr(test1))

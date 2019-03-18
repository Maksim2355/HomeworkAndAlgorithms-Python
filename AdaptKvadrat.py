from math import sin

x_min = float(input("Введите минимальное значение X:"))
x_max = float(input("Введите максимальное значение X:"))
max_slice_error = float(input("Введите максимальное значение погрешности:"))
num_intervals = int(input("Введите число разбиений:"))


def function(x):
    y = 1 + x + sin(2*x)
    return y


x1 = x_min
x2 = x_max


def slice_area(x1, x2, max_slice_error ):
    y1 = function(x1)
    y2 = function(x2)
    xm = (x1 + x2) / 2
    ym = function(xm)
    area12 = (x2 - x1) * (y1 + y2) / 2.0
    area1m = (xm - x1) * (y1 + ym) / 2.0
    aream2 = (x2 - xm) * (ym + y2) / 2.0
    area1m2 = area1m + aream2
    error = (area1m2 - area12) / area12
    if (abs(error) < max_slice_error):
        return area1m2
    else:
        return slice_area(x1, xm, max_slice_error) + slice_area(xm, x2, max_slice_error)


def useAdaptiveTrapezoidRule(x_min, x_max, num_intervals, max_slice_error):
    dx = (x_max - x_min) / num_intervals
    total_area = 0
    x = x_min
    for i in range(num_intervals):
        total_area = total_area + slice_area(x, x + dx, max_slice_error)
        x = x + dx
    return total_area

print(useAdaptiveTrapezoidRule(x_min, x_max, num_intervals, max_slice_error))
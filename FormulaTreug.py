from math import sin


def fn(x):
    return 1 + x + sin(x)


def rect_integral(function ,xmin, xmax, num_intervals):
    dx = (xmax-xmin)/num_intervals
    area = 0
    x = xmin
    for i in range(num_intervals):
        area += dx*function(x)
        x = x + dx
    return area

print("rect_integral = {}".format(rect_integral(fn,10,100,1000)))
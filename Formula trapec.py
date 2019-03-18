from math import sin
x_min = float(input("Введите значение минимального x:"))
x_max = float(input("Введите значение максимального x:"))
num_intervals = int(input("Введите значение точек:"))
x = x_min
dx = (x_max - x_min) / num_intervals
total_area = 0


def function(x):
    return 1 + x + sin(2*x)


for i in range(num_intervals):
    total_area = total_area + dx * (function(x) +
function(x + dx)) / 2
    x = x + dx

print(total_area)
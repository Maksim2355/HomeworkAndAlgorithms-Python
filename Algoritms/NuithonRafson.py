import math
inital_guess = float(input("Выберите начальное приближение "))


def fun(x):
    y = math.cos(x) - x**3
    return y


def fun2(x):
    y = - math.sin(x) - 3 * x**2
    return y


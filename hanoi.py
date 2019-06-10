def hanoi(n, a, b, c):
    if n > 1:
        hanoi(n-1, a, c, b)
        print(a, " -> ", b)
        hanoi(n-1, c, b, a)
    else:
        print(a, " -> ", b)

hanoi(3, 1, 2, 3)
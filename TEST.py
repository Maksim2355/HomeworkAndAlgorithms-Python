def sort_stack(s):
    t = []
    while s:                          # (1)
        x = s.pop()
        while t and t[-1] > x:        # (2)
            s.append(t.pop())         # (3)
        t.append(x)                   # (4)
    return t
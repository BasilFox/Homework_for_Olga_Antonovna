def f(x, y, p):
    if x + y >= 74 and p == 3:
        return 1
    elif x + y >= 74 and p != 3:
        return 0
    elif x + y < 74 and p > 3:
        return 0
    else:
        if p % 2 == 0:
            return f(x + 2, y, p + 1) or f(x * 2, y, p + 1) or f(x, y + 2, p + 1) or f(x, y * 2,
                                                                                       p + 1)
        else:
            return f(x + 2, y, p + 1) and f(x * 2, y, p + 1) and f(x, y + 2, p + 1) and f(x, y * 2,
                                                                                          p + 1)


for i in range(1, 67):
    if f(7, i, 0):
        print(i)

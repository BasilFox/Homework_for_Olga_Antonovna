def f(x, y, p):
    if x + y >= 77 and (p == 4 or p == 2):
        return 1
    elif x + y >= 77 and p % 2 != 0:
        return 0
    elif x + y < 77 and p > 4:
        return 0
    else:
        if p % 2 == 1:
            return f(x + 1, y, p + 1) or f(x * 2, y, p + 1) or f(x, y + 1, p + 1) or f(x, y * 2,
                                                                                       p + 1)
        else:
            return f(x + 1, y, p + 1) and f(x * 2, y, p + 1) and f(x, y + 1, p + 1) and f(x, y * 2,
                                                                                          p + 1)


def f1(x, y, p):
    if x + y >= 77 and p == 2:
        return 1
    elif x + y >= 77 and p != 2:
        return 0
    elif x + y < 77 and p > 2:
        return 0
    else:
        if p % 2 == 1:
            return f1(x + 1, y, p + 1) or f1(x * 2, y, p + 1) or f1(x, y + 1, p + 1) or f1(x, y * 2,
                                                                                           p + 1)
        else:
            return f1(x + 1, y, p + 1) and f1(x * 2, y, p + 1) and f1(x, y + 1, p + 1) and f1(x,
                                                                                              y * 2,
                                                                                              p + 1)


for i in range(1, 70):
    if f(7, i, 0):
        print(i)
print('**********************')
for i in range(1, 70):
    if f1(7, i, 0):
        print(i)

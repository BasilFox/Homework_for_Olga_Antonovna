def f(x, p):
    if x >= 65 or p > 3:
        if x < 100:
            return p == 3
        else:
            return False
    if p % 2 == 0:
        return f(x + 1, p + 1) or f(x * 3, p + 1)
    else:
        return f(x + 1, p + 1) and f(x * 3, p + 1)


for i in range(65):
    if f(i, 0):
        print(i)

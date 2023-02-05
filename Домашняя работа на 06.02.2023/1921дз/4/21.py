def f(x, y, p):
    if x + y <= 18 or p > 4:
        return p == 2 or p == 4
    if p % 2 == 1:
        return f(x - 1, y, p + 1) or f(x // 2, y, p + 1) or f(x, y - 1, p + 1) or f(x, y // 2, p + 1)
    else:
        return f(x - 1, y, p + 1) and f(x // 2, y, p + 1) and f(x, y - 1, p + 1) and f(x, y // 2,
                                                                                       p + 1)


for i in range(1, 50):
    if f(i, i, 0):
        print(i)
# ответ 13

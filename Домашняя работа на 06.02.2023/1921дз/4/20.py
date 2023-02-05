def f(x, y, p):
    if x + y <= 18 or p > 3:
        return p == 3
    if p % 2 == 0:
        return f(x - 1, y, p + 1) or f(x // 2, y, p + 1) or f(x, y - 1, p + 1) or f(x, y // 2, p + 1)
    else:
        return f(x - 1, y, p + 1) and f(x // 2, y, p + 1) and f(x, y - 1, p + 1) and f(x, y // 2,
                                                                                       p + 1)


for i in range(1, 50):
    if f(13, i, 0):
        print(i)
# ответ 14, 27
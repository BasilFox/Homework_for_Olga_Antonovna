def f(x, y, p):
    if x + y <= 18 or p > 2:
        return p == 2
    return f(x - 1, y, p + 1) or f(x // 2, y, p + 1) or f(x, y - 1, p + 1) or f(x, y // 2, p + 1)


for i in range(1, 50):
    if f(i, i, 0):
        print(i, i)
# ответ 10

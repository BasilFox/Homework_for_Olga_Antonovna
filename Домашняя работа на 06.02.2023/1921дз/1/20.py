def f(x, y, p):
    if x + y >= 45 or p > 3:
        return p == 3
    if p % 2 == 0:
        return f(x + y, y, p + 1) or f(x, x + y, p + 1)
    else:
        return f(x + y, y, p + 1) and f(x, x + y, p + 1)


for i in range(50):
    if f(6, i, 0):
        print(i)

# ответ 7,13
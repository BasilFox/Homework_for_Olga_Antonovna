def f(x, y, p):
    if x + y >= 45 or p > 4:
        return p == 4
    if p % 2 == 1:
        return f(x + y, y, p + 1) or f(x, x + y, p + 1)
    else:
        return f(x + y, y, p + 1) and f(x, x + y, p + 1)


for i in range(50):
    if f(i, i, 0):
        print(i)
        break

# ответ 4


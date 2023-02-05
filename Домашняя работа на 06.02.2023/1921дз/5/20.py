def f(x, p):
    if x <= 10 or p > 3:
        return p == 3
    if p % 2 == 0:
        return f(x - 10, p + 1) or f(x // 3, p + 1)
    else:
        return f(x - 10, p + 1) and f(x // 3, p + 1)


for i in range(10000000000000000000000000):
    if f(i, 0):
        print(i)

# ответ 43 128

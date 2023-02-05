def f(x, p):
    if x <= 10 or p > 2:
        return p == 2
    return f(x - 10, p + 1) or f(x // 3, p + 1)


for i in range(5000, 1, -1):
    if f(i, 0):
        print(i)
        break
# ответ 98

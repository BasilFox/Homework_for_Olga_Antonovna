def f(x, p):
    if x >= 165 or p > 2:
        return p == 2
    # if p % 2 == 0:
    return f(x - 1, p + 1) or f(x * 2, p + 1)
    # else:
    #     return f(x - 1, p + 1) and f(x * 2, p + 1)


for i in range(1, 1000):
    if f(i, 0):
        print(i)
        break
# ответ 42

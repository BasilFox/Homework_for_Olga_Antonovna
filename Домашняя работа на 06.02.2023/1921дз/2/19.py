def f(x, p):
    if x >= 65 or p > 2:
        if x < 100:
            return p == 2
        else:
            return False
    return f(x + 1, p + 1) or f(x * 3, p + 1)


for i in range(65):
    if f(i, 0):
        print(i)
# ответ 8
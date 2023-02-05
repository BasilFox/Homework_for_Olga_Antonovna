def f(x, y, p):
    if x + y >= 45 or p > 2:
        return p == 2
    return f(x + y, y, p+1) or f(x, x + y, p+1)


for i in range(50):
    if f(7, i, 0):
        print(i)
        break
# ответ 11
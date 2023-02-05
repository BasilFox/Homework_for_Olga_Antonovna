def f(x, p):
    if x <= 10 or p > 4:
        return p == 2 or p == 4
    if p % 2 == 1:
        return f(x - 10, p + 1) or f(x // 3, p + 1)
    else:
        return f(x - 10, p + 1) and f(x // 3, p + 1)


count = 0
for i in range(1000000):
    if f(i, 0):
        count += 1
print(count)
# ответ 30

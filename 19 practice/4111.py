def f(x, p):
    if (x >= 65 and x <= 100) and (p == 2 or p==4):
        return 1
    elif x > 100 and (p == 3 or p==1):
        return 1
    elif x > 100 and (p == 4 or p==2):
        return 0
    elif x >= 65 and (p != 2 or p!=4):
        return 0
    elif x < 65 and p > 4:
        return 0
    else:
        if p % 2 == 1:
            return f(x + 1, p + 1) or f(x * 3, p + 1)
        else:
            return f(x + 1, p + 1) and f(x * 3, p + 1)

def f1(x, p):
    if (x >= 65 and x <= 100) and p == 2:
        return 1
    elif x > 100 and p == 1:
        return 1
    elif x > 100 and p == 2:
        return 0
    elif x >= 65 and p != 2:
        return 0
    elif x < 65 and p > 2:
        return 0
    else:
        if p % 2 == 1:
            return f1(x + 1, p + 1) or f1(x * 3, p + 1)
        else:
            return f1(x + 1, p + 1) and f1(x * 3, p + 1)

for i in range(1, 65):
    if f(i, 0):
        print(i)
for i in range(1, 65):
    if f1(i, 0):
        print(i)
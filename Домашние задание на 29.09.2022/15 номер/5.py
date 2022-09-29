flag = True
for A in range(0, 2000):
    flag = True
    for x in range(3000):
        if flag is False:
            break
        for y in range(3000):
            f = (2 * y + x != 70) or (x < y) or (A < x)
            if f is False:
                flag = False
                break
    if flag is True:
        print(A)

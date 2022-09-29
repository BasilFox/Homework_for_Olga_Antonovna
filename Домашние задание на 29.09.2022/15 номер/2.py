flag = True
for A in range(0, 1000):
    flag = True
    for x in range(5000):
        if flag is False:
            break
        for y in range(5000):
            f = (x + y <= 22) or (y <= x - 6) or (y >= A)
            if f is False:
                flag = False
                break
    if flag is True:
        print(A)

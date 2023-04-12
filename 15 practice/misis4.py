
for A in range(1000):
    flag = True
    for x in range(1000):
        f = (x & 29 != 0) <= ((x & 17 == 0) <= (x & A != 0))
        if f is False:
            flag = False
            break
    if flag:
        print(A)
        break

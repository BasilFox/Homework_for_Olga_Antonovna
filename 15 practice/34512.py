for A in range(1, 100):
    flag = True
    for x in range(1000):
        f = (x & 77 != 0) <= ((x & 12 == 0) <= (x & A != 0))
        if f is False:
            flag = False
            break
    if flag is True:
        print(A)
        break

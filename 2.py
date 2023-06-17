for i in range(50):
    ch = 64 ** 11 - 4 ** 10 + 96 - i
    summ = []
    while ch != 0:
        summ.append(ch % 4)
        ch = ch // 4
    if sum(summ)==71:
        print(i)
        break
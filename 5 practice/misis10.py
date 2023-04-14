for i in range(10000000000):
    k = bin(i)[2:]
    if i % 2 == 0:
        k = k + '00'
    else:
        k = k + '11'
    if int(k, 2) > 115:
        print(i)
        break

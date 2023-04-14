for i in range(161, 512):
    k = bin(i)[2:]
    if len(k) < 9:
        k = '0' * (9 - len(k)) + k
    k = k[:3] + k[6:]
    k = k[::-1]
    k = int(k, 2)
    # k = int(k[::-1], 2)
    st = ''
    while k != 0:
        st = str(k % 5) + st
        k = k // 5
    if st == 1:
        print(i)

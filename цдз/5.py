for i in range(100, 1000):
    sp = sorted(list(str(i)))
    maxch = str(sp[-1]) + str(sp[-2])
    flag = True
    minch=0
    if '0' in sp:
        while '0' in sp:
            sp.remove('0')
        minch = str(sp[0]) + '0'
        flag = False
    if len(sp) == 1:
        continue
    print(sp)
    if flag is True:
        minch = str(sp[0]) + str(sp[1])
    if int(maxch)-int(minch)==40:
        print(i)
        break

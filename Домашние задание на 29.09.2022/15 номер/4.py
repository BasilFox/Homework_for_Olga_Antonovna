def delen(ch, lit):
    if ch % lit == 0:
        return True
    else:
        return False


flag = True
for A in range(1,500):
    flag = True
    for x in range(1, 100000):
        f = not (delen(A, 25) and delen(x, 24) and delen(x, 75)) or delen(x, A)
        if f is False:
            flag = False
    if flag is True:
        print(A)

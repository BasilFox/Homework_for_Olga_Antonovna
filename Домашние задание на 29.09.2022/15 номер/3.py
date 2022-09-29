def delen(ch, lit):
    if ch % lit == 0:
        return True
    else:
        return False


flag = True
for A in range(100):
    flag = True
    for x in range(1000):
        f = (not (delen(x, 2)) or not (delen(x, 3))) or (x + A >= 80)
        if f is False:
            flag = False
    if flag is True:
        print(A)
        break

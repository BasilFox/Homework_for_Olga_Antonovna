def system(n, osn):
    st = ''
    while n != 0:
        st = str(n % osn) + st
        n = n // osn
    return st


for i in range(10000000000000000):
    k = system(i, 3)
    k = k + str(i % 3)
    if int(k, 3) > 1000:
        print(int(k, 3))
        break
# 1003

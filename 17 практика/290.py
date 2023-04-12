f = list(map(int, open('17-290.txt').readlines()))


def system(n, osn):
    itog = ''
    if n ==0:
        return '0'
    while n != 0:
        itog = str(n % osn) + itog
        n = n // osn
    return itog.lstrip('0')


count = 0
maxrz = -99999999999999999
for i in range(len(f) - 2):
    a = f[i]
    b = f[i + 1]
    w = f[i + 2]
    if system(a, 5)[-1] == '1' or system(b, 5)[-1] == '1' or system(w, 5)[-1] == '1':
        if len(system(a, 6)) == 4 and len(system(b, 6)) == 4 and len(system(w, 6)) == 4:
            count += 1
            rz = max(a, b, w) - min(a, b, w)
            maxrz = max(maxrz, rz)
print(count, maxrz)

f = list(map(int, open('5069.txt').readlines()))


def system(n, k):
    ch = ''
    if n ==0:
        return '0'
    while n != 0:
        ch = str(n % k) + ch
        n = n // k
    return ch


count = 0
maximum = -454645
for i in range(len(f) - 2):
    a = f[i]
    b = f[i + 1]
    z = f[i + 2]
    if system(a, 5)[-1] == '4' or system(b, 5)[-1] == '4' or system(z, 5)[-1] == '4':
        if system(a, 6).count('0') == 0 and system(b, 6).count('0') == 0 and system(z, 6).count(
                '0') == 0:
            count += 1
            maximum = max(maximum, (max(a, b, z) - min(a, b, z)))
print(count, maximum)

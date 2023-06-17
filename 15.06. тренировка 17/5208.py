f = list(map(int, open('5208.txt').readlines()))


def good(a, b):
    if len(str(a)) == 4 and len(str(b)) == 4 and a % 2 == 0 and b % 2 == 0 and str(a + b)[-1] + \
            str(a + b)[-2] == '44':
        return True


sp = []
for i in f:
    if i % 202 == 0:
        sp.append(i)
maxim = max(sp)
count = 0
minimal = 654654654564654564564654654
for i in range(len(f) - 2):
    if f[i] + f[i + 1] + f[i + 2] <= maxim:
        continue
    if good(f[i], f[i + 1]) or good(f[i], f[i + 2]) or good(f[i + 1], f[i + 2]):
        count += 1
        minimal = min(minimal, f[i] + f[i + 1] + f[i + 2])
print(count, minimal)

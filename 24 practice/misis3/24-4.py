f = open('24(4).txt').read()
sp = []
for i in range(len(f) - 2):
    if f[i] == f[i + 2]:
        sp.append(f[i + 1])
print(max(sp, key=sp.count))

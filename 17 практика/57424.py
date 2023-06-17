f = list(map(int, open('1_17.txt').readlines()))
sp = []
for i in f:
    if i >= 10 and i < 100:
        sp.append(i)
maxd = max(sp)
count = 0
maxch = -6465
for i in range(len(f) - 1):
    k = f[i]
    w = f[i + 1]
    k1 = str(k)
    w1 = str(w)
    if (len(k1) == 2 or len(w1) == 2) and (len(w1) != len(k1)) and (k + w) % maxd == 0:
        count += 1
        maxch = max(maxch, k + w)
print(count, maxch)

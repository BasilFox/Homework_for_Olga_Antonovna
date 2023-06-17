f = list(map(int, open('4688.txt').readlines()))
sp = []
for i in f:
    if i % 19 == 0:
        sp.append(i)
nai = max(sp)
count = 0
maxim = 5616515641465
for i in range(len(f) - 1):
    if f[i] > nai or f[i + 1] > nai:
        count += 1
        maxim = min(maxim, f[i] + f[i + 1])
print(count,maxim)

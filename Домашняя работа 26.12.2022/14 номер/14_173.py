chislo = 9 ** 7 + 3 ** 21 - 8
sp = []

while chislo != 0:
    sp.append(chislo % 3)
    chislo = chislo // 3
print(sum(sp))


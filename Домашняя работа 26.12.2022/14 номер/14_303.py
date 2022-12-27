chislo = 4 ** 1103 + 3 * 4 ** 1444 - 2 * 4 ** 144 + 66
sp = []
while chislo != 0:
    sp.append(chislo % 4)
    chislo = chislo // 4
print(sum(sp))

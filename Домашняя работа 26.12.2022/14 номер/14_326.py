chislo = 8 ** 888 + 16 * 16 ** 1616 - 2 ** 444
chislo = list(map(int, list(oct(chislo)[2:])))
print(chislo.count(max(chislo)))

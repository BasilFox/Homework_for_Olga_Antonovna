total = 0
for x1 in range(7, 8):
    for x2 in range(0, 7):
        for x3 in range(0, 7):
            for x4 in range(0, 7):
                for x5 in range(0, 7):
                    chislo = str(x1) + str(x2) + str(x3) + str(x4) + str(x5)
                    if '65' in chislo and '56' in chislo:
                        continue
                    if '65' in chislo or '56' in chislo:
                        if int(chislo, 8) % 2 == 0:
                            print(chislo, ' ', int(chislo, 8))
                            total += 1
print(total)
# ответ 130
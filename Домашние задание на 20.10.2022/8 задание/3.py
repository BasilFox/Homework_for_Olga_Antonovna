from itertools import product

sp = list(map(''.join, list(product('ОГЭИНФ', repeat=6))))
#print(sp)
total = 0
for i in sp:
    if i[0] != "Э" and i[0] != "О":
        continue
    if i[4:] != 'НФ':
        continue
    if 'ОГЭ' in i:
        continue
    if 'ИГ' not in i:
        continue
    total += 1
    print(i)
print(total)

# ответ 24
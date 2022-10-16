from itertools import product

sp = list(map(''.join, list(product('ОБЩЕСТВ', repeat=5))))
#print(sp)
total = 0
for i in sp:
    if i[0] == "Щ" or i[0] == "Б":
        continue
    if i[3:] != 'ВВ':
        continue
    if 'ЕВ' in i or 'ВЕ' in i:
        continue
    if 'ТБ' not in i:
        continue
    total += 1
    print(i)
print(total)
# ответ 11
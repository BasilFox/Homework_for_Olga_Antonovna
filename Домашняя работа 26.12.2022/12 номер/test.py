def prost(chislo):
    sp = []
    for i in range(1, chislo + 1):
        if chislo % i == 0:
            sp.append(i)
    if len(sp) == 2:
        return True
    else:
        return False


total = 0

for n in range(1, 100):
    stroka = '1' + '0' * n
    while '10' in stroka:
        if '10' in stroka:
            stroka = stroka.replace('10', '001', 1)
        if '1' in stroka:
            stroka = stroka.replace('1', '01', 1)
        print(stroka)
    stroka = stroka.lstrip('0')
    if prost(int(stroka)):
        total += 1
print(total)

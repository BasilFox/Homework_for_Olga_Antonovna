stroka = '>' + '1' * 20 + '2' * 15 + '3' * 40
while '>1' in stroka or '>2' in stroka or '>3' in stroka:
    if '>1' in stroka:
        stroka = stroka.replace('>1', '22>', 1)
    if '>2' in stroka:
        stroka = stroka.replace('>2', '2>1', 1)
    if '>3' in stroka:
        stroka = stroka.replace('>3', '1>2', 1)
stroka = stroka.replace('>', '')
stroka = map(int, list(stroka))
print(sum(stroka))
# ответ 450

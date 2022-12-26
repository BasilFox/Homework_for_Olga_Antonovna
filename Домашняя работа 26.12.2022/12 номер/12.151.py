stroka = '7' * 186
while '4444' in stroka or '777' in stroka:
    if '4444' in stroka:
        stroka = stroka.replace('4444', '77', 1)
    else:
        stroka = stroka.replace('777', '4', 1)
print(stroka)

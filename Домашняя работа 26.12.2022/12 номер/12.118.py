stroka = '8' * 93
while '222' in stroka or '888' in stroka:
    if '222' in stroka:
        stroka = stroka.replace('222', '8', 1)
    else:
        stroka = stroka.replace('888', '2', 1)
print(stroka)

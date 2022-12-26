n = 301
stroka = '8' * n
while True:
    stroka = '8' * n
    while '555' in stroka or '888' in stroka:
        stroka = stroka.replace('555', '8', 1)
        stroka = stroka.replace('888', '55', 1)
    if stroka.count('8')==1 and stroka.count('5')==1:
        print(n)
        break
    else:
        n+=1

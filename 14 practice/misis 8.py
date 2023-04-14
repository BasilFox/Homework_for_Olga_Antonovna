alf = '0123456789ABCDE'
for i in alf:
    ch = int(f'123{i}5', 15) + int(f'1{i}233', 15)
    if ch%14==0:
        print(ch//14)

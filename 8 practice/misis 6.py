st = 'ВЛТУ'
sp = sorted(st)
count=0
for x1 in sp:
    for x2 in sp:
        for x3 in sp:
            for x4 in sp:
                word = x1+x2+x3+x4
                count +=1
                if count==98:
                    print(word)
                    break
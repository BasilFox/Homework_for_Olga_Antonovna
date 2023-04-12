st = '12345'
cou = 0
for x1 in st:
    for x2 in st:
        for x3 in st:
            for x4 in st:
                for x5 in st:
                    code = x1+x2+x3+x4+x5
                    if code.count('1')==3:
                        cou +=1
print(cou)
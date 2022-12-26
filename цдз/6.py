slovo = "ОГД"
sp = set()
for x1 in slovo[1:]:
    for x2 in slovo:
        for x3 in slovo:
            for x4 in slovo:
                for x5 in slovo:
                    for x6 in slovo[1:]:
                        a = x1+x2+x3+x4+x5+x6
                        sp.add(a)
print(len(sp))
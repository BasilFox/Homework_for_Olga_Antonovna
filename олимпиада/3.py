chisla = {112}


def drob(ishod):
    if ishod>0 and ishod ** 0.5 == int(ishod ** 0.5):
        return ishod - 2, ishod - 3, ishod ** 0.5
    else:
        return ishod - 2, ishod - 3


for i in range(17):
    newmn = set()
    for w in chisla:
        k = drob(w)
        newmn.add(k[0])
        newmn.add(k[1])
        if len(k) == 3:
            newmn.add(k[2])
    chisla=chisla.union(newmn)
print(len(chisla))

def system(chislo, osnova):
    sp = []
    while chislo != 0:
        sp.append(str(chislo % osnova))
        chislo = chislo // osnova
    return sp[::-1]


for i in range(2, 10):
    print(i)
    print(system(123, i))

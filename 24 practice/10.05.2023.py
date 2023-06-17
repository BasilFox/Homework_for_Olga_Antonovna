f = open('24.txt').read()
alf = []
st = 'XYZ'
for x1 in st:
    for x2 in st:
        for x3 in st:
            sp = [x1,x2,x3]
            if len(sp)==len(set(sp)):
                alf.append((x1 + x2 + x3))
for i in alf:
    f = f.replace(i,'*')
f = f.split('*')
print(len(max(f,key=len)))

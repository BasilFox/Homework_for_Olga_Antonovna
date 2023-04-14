f = open('107_24.txt').read()
st = 'ABC'
f = f.replace('AB', '*')
f = f.replace('CB', '*')
for i in st:
    f = f.replace(i, ' ')
f = f.split()
print(len(max(f, key=len)))

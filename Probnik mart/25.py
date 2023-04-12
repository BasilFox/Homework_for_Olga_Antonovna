sp = [1]

for i in range(10):
    sp1 = []900*
    for w in sp:
        sp1.append(w + 4)
        sp1.append(w + 7)
        sp1.append(int(w / 2))
    sp = sp1[:]
    print(sp)
print(sp, sp.count(1))

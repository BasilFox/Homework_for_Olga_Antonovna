from itertools import product

sp = (list(map(''.join, list(product("ПАРУС", repeat=5)))))
sp = sorted(sp)
for i in sp:
    if i[0]!="У":
        continue
    else:
        flag = True
        for w in range(5):
            if i[w] == 'А' and i[w+1] == 'А':
                flag =False
                break
    if flag is True:
        print(i,sp.index(i))
        break

print(sp)
# ОТВЕТ 2526
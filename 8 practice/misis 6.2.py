ch = 'ABCD'
ch1 = 'XY'
cnt = 0
for x1 in ch1:
    for x2 in ch:
        for x3 in ch:
            for x4 in ch:
                slovo = x1 + x2 + x3 + x4
                cnt += 1
print(cnt)

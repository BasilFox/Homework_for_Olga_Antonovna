for i in range(2, 10000000000):
    k = bin(i)[2:]
    st = ''
    for w in k:
        if w == '1':
            st += '0'
        else:
            st += '1'
    st = st.rstrip('0')
    if st =='':
        continue
    if int(st, 2) == 817:
        print(i)
        break
#1230
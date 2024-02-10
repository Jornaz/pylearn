st = input()
lenght = len(st)
symb = st[0]
mx_cnt = 0

for i in range(lenght):
    if st.count(st[i]) >= mx_cnt:
        mx_cnt = st.count(st[i])
        symb = st[i]

print(symb)

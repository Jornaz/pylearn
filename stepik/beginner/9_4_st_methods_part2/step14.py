st = input()

cnt = 0

cnt = st.count('f')

if cnt == 0:
    print('NO')
elif cnt == 1:
    print(st.find('f'))
elif cnt > 1:
    print(st.find('f'), st.rfind('f'))
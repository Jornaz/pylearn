st = input()

lenght = len(st)

cnt = st.count('f')

if cnt == 1:
    print(-1)
elif cnt == 0:
    print(-2)
else:
    a = st.find('f')
    b = st.find('f',a+1)
    print(b)
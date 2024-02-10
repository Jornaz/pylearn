n = int(input())

st = ''
cnt = 0
for i in range(n):
    st = input()
    if st.count('11') >= 3:
        cnt += 1
print(cnt)
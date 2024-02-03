flag = True

for _ in range(10):
    if int(input())%2 != 0:
        flag = False

if flag == True:
    print('YES')
else:
    print('NO')

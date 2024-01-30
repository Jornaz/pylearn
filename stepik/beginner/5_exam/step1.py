num = int(input())

prelast = (num // 10) % 10
last = num % 10

if prelast == 0 and last == 0:
    print('YES')
else:
    print('NO')
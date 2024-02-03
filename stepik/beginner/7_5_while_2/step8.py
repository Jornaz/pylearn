num = int(input())
last = num % 10
flag = True

while num > 0:
    last_digit = num%10
    if last_digit != last:
        flag = False
    num = num // 10

if flag:
    print('YES')
else:
    print('NO')
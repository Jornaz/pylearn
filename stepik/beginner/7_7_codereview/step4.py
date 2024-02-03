n = int(input())
max_digit = 0
flag = False
while n > 0:
    digit = n % 10
    if digit % 3 == 0:
        if digit > max_digit:
            max_digit = digit
        flag = True
    n = n // 10
if flag == False:
    print('NO')
else:
    print(max_digit)
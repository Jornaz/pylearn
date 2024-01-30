num = int(input())

if num%2 == 1:
    print("YES")
else:
    if num%2 == 0 and 2<= num <=5:
        print('NO')
    if num%2 == 0 and 6 <= num <= 20:
        print('YES')
    if num%2 == 0 and num > 20:
        print('NO')
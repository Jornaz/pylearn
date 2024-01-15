a, b, c = int(input()), int(input()), int(input())

first = a + b > c
second = a + c > b
third = b + c > a

if first and second and third:
    print('YES')
else:
    print('NO')
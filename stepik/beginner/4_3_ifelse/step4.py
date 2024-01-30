a, b, c = int(input()), int(input()), int(input())

usl1m, usl2m, usl3m = 'Равносторонний', 'Равнобедренный', 'Разносторонний'

usl1 = a == b == c
usl2 = a == b or a == c or b == c
usl3 = a != b and a != c and b != c

if usl1:
    print(usl1m)
elif usl2:
    print(usl2m)
elif usl3:
    print(usl3m)

a, b = int(input()), int(input())
c = str(input())
if c == '+' or c == '-' or c == '*' or c == '/':
    #Сложение
    if c == '+':
        print(a+b)
    #Вычитание
    if c == '-':
        print(a-b)
    #Умножение
    if c == "*":
        print(a*b)
    #Деление
    if c == '/' and b == 0:
        print('На ноль делить нельзя!')    
    if c == '/' and b != 0:
        print(a/b)
else:
    print('Неверная операция')
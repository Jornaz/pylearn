num = int(input())

#Проверяем чтобы число было от 0 до 36
iscorrenct = 0 <= num <= 36

green = 'зеленый'
red = 'красный'
black = 'черный'

if iscorrenct:
    if num == 0:
        print(green)
    if 1 <= num <= 10:
        if num%2 == 1:
            print(red)
        else:
            print(black)
    if 11 <= num <= 18:
        if num%2 == 1:
            print(black)
        else:
            print(red)
    if 19 <= num <= 28:
        if num%2 == 1:
            print(red)
        else:
            print(black) 
    if 29 <= num <= 36:
        if num%2 == 1:
            print(black)
        else:
            print(red)
else:
    print('ошибка ввода')
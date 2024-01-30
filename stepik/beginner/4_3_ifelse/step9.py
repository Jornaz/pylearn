col1, col2 = str(input()), str(input())

red = 'красный'
blue = 'синий'
yellow = 'желтый'

#Проверяем правильность ввода
check1 = col1 == red or col1 == blue or col1 == yellow
check2 = col2 == red or col2 == blue or col2 == yellow
iscorrect = check1 and check2

purple = 'фиолетовый'
orange = 'оранжевый'
green = 'зеленый'

if iscorrect:
    #purple = red and blue
    if (col1 == red and col2 == blue) or (col1 == blue and col2 == red):
        print(purple)
    #orange = red and yellow
    if (col1 == red and col2 == yellow) or (col1 == yellow and col2 == red):
        print(orange)    
    #green = blue and yellow
    if (col1 == blue and col2 == yellow) or (col1 == yellow and col2 == blue):
        print(green)
    #red
    if col1 == red and col2 == red:
        print(red)
    #blue
    if col1 == blue and col2 == blue:
        print(blue)
    #yellow
    if col1 == yellow and col2 == yellow:
        print(yellow)
else:
    print('ошибка цвета')
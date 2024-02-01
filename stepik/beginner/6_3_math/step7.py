import math

a, b, c = float(input()), float(input()), float(input())

#квдратное уравнение ax^2+bx+c=0

D = (b**2) - (4*a*c)

if D<0:
    print('Нет корней')
elif D == 0:
    x1 = (-1*b)/(2*a)
    print(x1)
else:
    x1 = (-1*b-math.sqrt(D))/(2*a)
    x2 = (-1*b+math.sqrt(D))/(2*a)
    print(min(x1,x2))
    print(max(x1,x2))
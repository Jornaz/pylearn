a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())

# a1b1 - 1 отрезок a2b2 - второй отрезок

#пустое множество:
if b1 < a2 or b2 < a1:
    print('пустое множество')

#точка пересечения
if b1 == a2:
    print(b1)

if a1 == b2:
    print(a1)

#отрезок пересечения
    
if a1 <= a2 < b1 < b2:
    print(a2, b1)

if a2 <= a1 < b2 < b1:
    print(a1, b2)

if a1 < a2 < b2 <= b1:
    print(a2,b2)

if a2 < a1 < b1 <= b2:
    print(a1,b1)

if a1 == a2 and b1 == b2:
    print(a1,b1)
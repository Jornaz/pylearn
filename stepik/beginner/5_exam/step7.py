x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

dx = abs(x1 - x2)
dy = abs(y1 - y2)

#dy может быть 1 или 2 или -1 и -2
#dx аналогично
if (dy == 1 and dx == 2) or (dy == 2 and dx ==1):
    print('YES')
else:
    print('NO')
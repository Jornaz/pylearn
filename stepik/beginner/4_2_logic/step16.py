x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

dx = x2 - x1
dy = y2 - y1

if (dx == 1 or dx == 0 or dx == -1) and (dy == 1 or dy == 0 or dy == -1) :
    print('YES')
else:
    print('NO')

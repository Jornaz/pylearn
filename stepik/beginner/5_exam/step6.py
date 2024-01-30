x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

dx = x1 - x2
dy = y1 - y2
if dy !=0:
    if (dx/dy == 1) or (dx/dy == -1):
        print('YES')
    else:
        print('NO')
else:
    print('NO')
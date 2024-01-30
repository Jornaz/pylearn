x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

dx = abs(x1 - x2)
dy = abs(y1 - y2)

if dy >= 0 and (dx - dy == 0):
    print('YES')
elif dy == 0 and dx > 0:
    print('YES')
elif dy > 0 and dx == 0:
    print('YES')
else:
    print('NO')

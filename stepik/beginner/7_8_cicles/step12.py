#10x+5y+0,5z = 100, x+y+z=100

for x in range(1, 100):
    for y in range(1, 100):
        for z in range(1, 100):
            if 10 * x + 5 * y + 0.5 * z == 100:
                if x + y + z == 100:
                    print('x =', x, 'y =', y, 'z =', z)
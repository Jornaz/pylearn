total = 0
for a in range(133, 134):
    for b in range(110, 111):
        for c in range(84, 85):
            for d in range(27, 28):
                for e in range(144, 145):
                    if a ** 5 + b ** 5 + c ** 5 + d ** 5 == e ** 5:
                        total += 1
                        print(a, b, c, d, e)
                        print('a + b + c + d + e =', a + b + c + d + e)
    print('Общее количество натуральных решений =', total)
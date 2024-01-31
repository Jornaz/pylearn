city1, city2, city3 = input(), input(), input()

a, b, c = len(city1), len(city2), len(city3)

short = min(a, b, c)
biggest = max(a, b, c)

if short == a:
    print(city1)
elif short == b:
    print(city2)
else:
    print(city3)

if biggest == a:
    print(city1)
elif biggest == b:
    print(city2)
else:
    print(city3)
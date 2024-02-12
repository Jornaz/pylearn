st = input()

lenght = len(st)

for i in range(lenght):
    if i % 3 == 0:
        continue
    print(st[i], end = '')
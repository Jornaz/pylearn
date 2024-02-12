st = input()

lenght = len(st)

for i in range(lenght):
    if st[i] == '@':
        continue
    print(st[i], end = '')
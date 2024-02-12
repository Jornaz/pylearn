st = input()

lenght = len(st)

for i in range(lenght):
    if st[i] == '1':
        print('one', end = '')
        continue
    print(st[i], end = '')
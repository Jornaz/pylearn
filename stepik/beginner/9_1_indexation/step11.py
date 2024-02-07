st = input()
lenght = len(st)
num = '1234567890'
flag = False
for i in range(lenght):
    if st[i] in num:
        flag = True
        break
if flag:
    print('Цифра')
else:
    print('Цифр нет')
st = input()
lenght = len(st)
cnt_plus = 0
cnt_mult = 0

for i in range(lenght):
    if st[i] == '+':
        cnt_plus += 1
    elif st[i] == '*':
        cnt_mult += 1

print('Символ + встречается', cnt_plus, 'раз')
print('Символ * встречается', cnt_mult, 'раз')
st = input()
lenght = len(st)
cnt_glas = 0
cnt_soglas = 0

glas = 'АУОЫИЭЯЮЁЕауоыиэяюёе'
soglas = 'БВГДЖЗЙКЛМНПРСТФХЦЧШЩбвгджзйклмнпрстфхцчшщ'

for i in range(lenght):
    if st[i] in glas:
        cnt_glas += 1
    elif st[i] in soglas:
        cnt_soglas += 1

print('Количество гласных букв равно', cnt_glas)
print('Количество согласных букв равно', cnt_soglas)
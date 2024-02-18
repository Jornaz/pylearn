ip = input()

adr = ip.split('.')

flag = True
for i in range(4):
    if 0 <= int(adr[i]) <= 255:
        continue
    flag = False

if flag:
    print('ДА')
else:
    print('НЕТ')
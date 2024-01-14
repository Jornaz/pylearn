abcd = int(input())

a = abcd // 1000
b = (abcd// 100) % 10
c = (abcd // 10) % 10
d = abcd % 10

uslovie = a+d == b-c

if uslovie:
    print('ДА')
else:
    print('НЕТ')

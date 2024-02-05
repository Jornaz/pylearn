n = int(input())

ch ='*'
dx = 1

for i in range(1, n //2+2):
    for j in range(i):
        print(ch, end = '')
    print()
for i in range(n // 2, 0, -1):
    for j in range(i):
        print(ch, end = '')
    print()
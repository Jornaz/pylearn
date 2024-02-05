n = 8
count = 0
maximum = -1000000000000
for i in range(1, n + 1):
    x = int(input())
    if x % 4 == 0:
        count += 1
        if x > maximum:
            maximum = x
if count > 0:
    print(count)
    print(maximum)
elif count <= 0:
    print('NO')
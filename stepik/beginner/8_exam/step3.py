n = 4
count = 0
maximum = -100000000
for i in range(1, n + 1):
    x = int(input())
    if x % 2 != 0:
        count += 1
        if x > maximum:
            maximum = x
            #break
if count > 0:
    print(count)
    print(maximum)
elif count <=0:
    print('NO')
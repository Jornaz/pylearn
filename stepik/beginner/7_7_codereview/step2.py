mx = - 1000000
total = 0
for i in range(10):
    x = int(input())
    if x < 0:
        total += x
    if x < 0 and x > mx:
        mx = x

if mx != -1000000:
    print(total)
    print(mx)
else:
    print('NO')
a, b = int(input()), int(input())
cnt = 0
for i in range(a, b+1):
    for j in range(1, b+1):
        if i%j == 0:
            cnt += 1
    if cnt == 2:
        print(i)
    cnt = 0
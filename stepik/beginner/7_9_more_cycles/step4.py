a = 1
b = int(input())
mx_cnt = 0
mx_total = 0
mx_number = 0
total = 0
cnt = 0
for i in range(a, b+1):
    for j in range(1, b+1):
        if i%j == 0:
            cnt += 1
            total += j
    print(i, '+' * cnt, sep = '')
    total = 0
    cnt = 0

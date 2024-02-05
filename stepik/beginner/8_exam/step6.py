n = int(input())
cnt_3 = 0
edge_num = n % 10
cnt_edge = 0
cnt_chet = 0
total_5 = 0
prz_7 = 1
total_0_5 = 0
while n > 0:
    last = n%10
    if last == 3:
        cnt_3 += 1
    if last == edge_num:
        cnt_edge += 1
    if last % 2 == 0:
        cnt_chet += 1
    if last > 5:
        total_5 += last
    if last > 7:
        prz_7 *= last
    n = n // 10
    if last == 0:
        total_0_5 += 1
    if last == 5:
        total_0_5 += 1
print(cnt_3)
print(cnt_edge)
print(cnt_chet)
print(total_5)
print(prz_7)
print(total_0_5)
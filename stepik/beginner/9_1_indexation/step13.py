st = input()

lenght = len(st)
cnt_same = 0

for i in range(lenght-1):
    if st[i] == st[i+1]:
        cnt_same += 1

print(cnt_same)
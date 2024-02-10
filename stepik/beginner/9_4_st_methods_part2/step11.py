st = input()

lenght = len(st)
cnt = 0

for i in range(lenght):
    if st[i].isdigit():
        cnt += 1

print(cnt)
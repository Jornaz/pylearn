st = input()
lenght = len(st)
cnt_lower = 0

for i in range(lenght):
    if st[i].islower():
        cnt_lower += 1 

print(cnt_lower)
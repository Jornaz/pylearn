n = int(input())
seq = []
for _ in range(n):
    seq.append(input())
k = int(input())
req = []
for j in range(k):
    key = input()
    for i in range(n):
        if key.lower() in seq[i].lower():
            req.append(seq[i])
lenght = len(req)
cnt = 1
#print(req)
#print(f'k = {k}')
fin = []
for i in range(lenght):
    for o in range(i, lenght):
        if i != o:
            if req[i] == req[o]:
                cnt += 1
    if cnt == k:
        fin.append(req[i])
    cnt = 1
print(*fin, sep = '\n')
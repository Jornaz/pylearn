n = int(input())
ls = []

for _ in range(n):
    ls.append(input())

k = int(input())

for i in range(n):
    if len(ls[i]) >= k:
        print(ls[i][k-1], end = '')
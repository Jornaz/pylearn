n = int(input())
ls = []

for _ in range(n):
    ls.append(int(input()))

del ls[1::2]

print(ls)
n = int(input())
ls = []
ls2 = []
for _ in range(n):
    ls.append(input())

for i in range(n):
    ls2.extend(ls[i])

print(ls2)
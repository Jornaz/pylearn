n = int(input())
ls1 = []
ls2 = []
for _ in range(n):
    ls1.append(int(input()))

lenght = len(ls1)

for i in range(lenght-1):
    ls2.append(sum(ls1[i:i+2]))

print(ls2)
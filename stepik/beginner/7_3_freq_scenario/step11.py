import math as m

n = int(input())
total = 0

for i in range(1, n+1):
    total += m.pow(-1, i+1)*i

print(int(total))
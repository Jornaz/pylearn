import math as m

n = int(input())
total = 0
for i in range(1, n+1):
    total += 1/i
total -= m.log(n)

print(total)
import math
n = int(input())
total = 0
for i in range(1, n+1):
    total += math.factorial(i)

print(total)
import math

a, b = int(input()), int(input())

# a <= b куб оканчивается на 4 или 9 
cnt = 0

for i in range(a, b+1):
    if math.pow(i,3)%10 == 4 or math.pow(i,3)%10 == 9:
        cnt += 1

print(cnt)
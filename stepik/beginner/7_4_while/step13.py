price = int(input())
cnt = 0

while price >= 25:
    cnt += 1
    price -= 25
while price >= 10:
    cnt += 1
    price -= 10
while price >= 5:
    cnt += 1
    price -= 5
while price >= 1:
    cnt += 1
    price -= 1

print(cnt)
n = int(input())

mx, mx2 = 2, 2

for _ in range(n):
    tmp = int(input())
    if tmp > mx2:
        mx2 = tmp
    if mx2 > mx:
        mx2, mx = mx, mx2

print(mx)
print(mx2)
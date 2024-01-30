a, b, c = int(input()), int(input()), int(input())

mid = a

if (b > a and b < c) or (b < a and b > c):
    mid = b
if (c > a and c < b) or (c < a and c > b):
    mid = c
print(mid)

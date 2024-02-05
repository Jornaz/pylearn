n = int(input())
s = 0
while n > 0:
    last = n%10
    if last % 2 == 0:
        s += last
    n //= 10
print(s)
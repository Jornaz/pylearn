n = int(input())
total = 0
while n > 0:
    last = n%10
    total += last
    n //= 10
    #print(last, total, n, sep = ' | ')
    if n == 0 and total > 9:
        n = total
        total = 0

print(total)
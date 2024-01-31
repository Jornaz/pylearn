n = int(input())

a = n // 100
b = (n // 10) % 10
c = n % 10

maxn = max(a,b,c)
minn = min(a,b,c)
midn = a+b+c- maxn - minn

if maxn - minn == midn:
    print('Число интересное')
else:
    print('Число неинтересное')
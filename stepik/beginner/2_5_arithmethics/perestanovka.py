abc = int(input())

an = abc // 100
bn = (abc// 10) % 10
cn = abc % 10

a, b, c = str(an), str(bn), str(cn)

print(a, b, c, sep='')
print(a, c, b, sep='')
print(b, a, c, sep='')
print(b, c, a, sep='')
print(c, a, b, sep='')
print(c, b, a, sep='')
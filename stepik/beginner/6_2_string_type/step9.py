str1, str2, str3 = input(), input(), input()

a, b, c = len(str1), len(str2), len(str3)

d = min(a,b,c)
f = max(a,b,c)
e = a + b + c - d - f

dx = abs(d - e)
dy = abs(e - f)

if dx == dy:
    print('YES')
else:
    print('NO')
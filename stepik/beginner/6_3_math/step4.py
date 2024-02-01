import math

a, b = float(input()), float(input())

res1 = (a+b)/2
res2 = math.sqrt(a*b)
res3 = (2*a*b)/(a+b)
res4 = math.sqrt((a**2+b**2)/2)

print(res1)
print(res2)
print(res3)
print(res4)
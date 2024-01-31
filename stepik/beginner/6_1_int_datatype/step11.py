num1, num2, num3 = int(input()), int(input()), int(input())

a = max(num1, num2, num3)
c = min(num1, num2, num3)

if num1 != a and num1 != c:
    b = num1
elif num2 != a and num2 != c:
    b = num2
else:
    b = num3

if b == c:
    b = a
    
print(a)
print(b)
print(c)
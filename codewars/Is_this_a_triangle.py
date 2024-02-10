a, b, c = int(input()), int(input()), int(input())

flag = False

if a + b > c:
    if a + c > b:
        if b + c > a:
            flag = True

print(flag)
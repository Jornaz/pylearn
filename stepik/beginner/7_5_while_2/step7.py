num = int(input())

while num > 0:
    last_digit = num%10
    if num // 10 > 0:
        result = num
    num = num // 10

result %= 10

print(result)
num = int(input())

mn, mx = num%10, num%10

while num > 0:
    last_digit = num%10
    if last_digit < mn:
        mn = last_digit
    if last_digit > mx:
        mx = last_digit
    num = num // 10

print('Максимальная цифра равна', mx)
print('Минимальная цифра равна', mn)
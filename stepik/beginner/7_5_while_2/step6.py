num = int(input())

total = 0
cnt = 0
prz = 1
mid = 0
first_digit = 0
last = num%10
first_and_last = 0

while num > 0:
    last_digit = num%10
    total += last_digit
    cnt += 1
    prz *= last_digit
    if num // 10 == 0:
        first_digit = num
    num = num // 10

mid = total / cnt
first_and_last = first_digit + last

print(total)
print(cnt)
print(prz)
print(mid)
print(first_digit)
print(first_and_last)
age = int(input())


if age == 1:
    result = 10.5
elif age == 2:
    result = int(10.5 * 2)
else:
    result = int(21 + (4*(age-2)))

print(result)
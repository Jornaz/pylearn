n = int(input())

first_d = n // 100
second_d = (n // 10) % 10
third_d = n % 10

summa = first_d + second_d + third_d
prz = first_d * second_d * third_d

print('Сумма цифр =', summa)
print('Произведение цифр =', prz)
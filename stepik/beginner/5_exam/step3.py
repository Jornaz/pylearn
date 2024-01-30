age = int(input())
gender = str(input())

age_filter = 10 <= age <=15
gender_filter = gender == 'f'

if age_filter and gender_filter:
    print('YES')
else:
    print('NO')
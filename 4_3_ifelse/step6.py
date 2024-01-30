num = int(input())

if 0 <= num <= 7: 
    result = 30 + num%2

if 8 <= num <= 12: 
    result = 30 + (num+1)%2

if num == 2:
    result = 28

print(result)
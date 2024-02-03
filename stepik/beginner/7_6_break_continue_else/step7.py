num = int(input())

delitel = 2

while num > 1:
    if num % delitel == 0:
        print(delitel)
        break
    delitel += 1
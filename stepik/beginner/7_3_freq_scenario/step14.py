n = int (input())

#n <=100

a, b = 0, 1

for _ in range(0, n):
    a, b = b, a +b
    print(a, end = ' ')
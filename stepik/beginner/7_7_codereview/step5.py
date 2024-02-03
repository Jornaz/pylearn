import math
n = int(input())
n = str(n)
lenght = len(n)
n = int(n)
n = n // math.pow(10, lenght -1)
print(int(n))

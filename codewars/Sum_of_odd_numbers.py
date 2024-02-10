n = int(input())
tmp = 1
result = 0
for i in range(1, n+1):
    for k in range(i):
        #print(tmp, end=' ')
        result += tmp
        tmp += 2
        if i == n and k == i-1:
            return result
    #print(result)
    result = 0
    #print()
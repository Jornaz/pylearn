n = int(input())

strings = []

for _ in range(n):
    tmp = input()
    if tmp not in strings:
        strings.append(tmp)


print(*strings, sep = '\n')

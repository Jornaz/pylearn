n = int(input())

edge = "*" * 19
content = '*' + ' ' * 17 + '*'
print(edge)
for _ in range(n-2):
    print(content)
print(edge)
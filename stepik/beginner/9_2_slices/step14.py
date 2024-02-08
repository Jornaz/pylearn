st = input()

lenght = len(st)
print(lenght)
if lenght%2 == 0:
    part1 = st[:lenght//2]
    part2 = st[lenght//2:]
else:
    part1 = st[:lenght//2+1]
    part2 = st[lenght//2+1:]
result = part2 + part1

print(result)
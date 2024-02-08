word = input()

polyndrom = False

if word == word[::-1]:
    polyndrom = True

if polyndrom:
    print('YES')
else:
    print('NO')
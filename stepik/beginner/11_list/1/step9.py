n = int(input())
# a-97 z - 122

alphabet = list(range(97, 97+n))

for i in range(n):
    alphabet[i] = chr(alphabet[i])

print(alphabet)
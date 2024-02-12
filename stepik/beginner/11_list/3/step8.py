alphabet = 'abcdefghijklmnopqrstuvwxyz'
rng = len(alphabet)
ls = []
for i in range(rng):
    ls.append(alphabet[i]*(i+1))

print(ls)
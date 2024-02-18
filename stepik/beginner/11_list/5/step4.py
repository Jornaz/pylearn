fio = input()

words = fio.split()
res = []
for i in range(3):
    res.append(words[i][0])
fin = ''    
fin += '.'.join(res)

print(f'{fin}.')
age = int(input())

gr1 = age <= 13
gr2 = 14 <= age <= 24
gr3 = 25 <= age <= 59
gr4 = age >= 60

if gr1:
    print('детство')
if gr2:
    print('молодость')
if gr3:
    print('зрелость')
if gr4:
    print('старость')
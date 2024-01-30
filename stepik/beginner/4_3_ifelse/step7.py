weight = int(input())

cat1m, cat2m, cat3m = 'Легкий вес', 'Первый полусредний вес', 'Полусредний вес'

cat1 = 0  <= weight < 60
cat2 = 60 <= weight < 64 
cat3 = 64 <= weight < 69

if cat1:
    print(cat1m)
if cat2:
    print(cat2m)
if cat3:
    print(cat3m)
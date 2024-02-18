n = int(input())
seq = []
for _ in range(n):
    seq.append(input())
req = input()

for i in range(n):
    if req.lower() in seq[i].lower():
        print(seq[i])
step = int(input())
st = input()
lenght = len(st)
# a-97 z - 122



for i in range(lenght):
    a = ord(st[i])
    #print(a)
    for k in range(step):
        a -= 1
        if a == 96:
            a = 122
            
    print(chr(a), end = '')


    
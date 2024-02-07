n = int(input())

result_num = ''

while n>0:
    mod = n%2
    result_num += str(mod)
    n //= 2
lenght = len(result_num)
new_result = ''
for i in range(-1, -lenght -1, -1):
    new_result += result_num[i]
    #print(i)
print(new_result)
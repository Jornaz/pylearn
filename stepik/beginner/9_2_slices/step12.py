st = input()

cnt_symb = len(st)
st_x3 = st * 3
first_symb = st[:1]
first_3 = st[:3]
last_3 = st[-3:]
reverse_st = st[::-1]
modified_st = st[1:-1]

print(cnt_symb)
print(st_x3)
print(first_symb)
print(first_3)
print(last_3)
print(reverse_st)
print(modified_st)
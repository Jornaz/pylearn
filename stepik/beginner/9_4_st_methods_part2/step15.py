st = input()

a = st.find('h')
b = st.rfind('h')+1

print(st[:a], st[b:], sep = '')
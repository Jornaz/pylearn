st = input()

lenght = len(st)

a = st.find('h')
b = st.rfind('h')

print(st[:a],st[b:a:-1],st[b:], sep = '')
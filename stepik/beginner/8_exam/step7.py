#x^3+y^3=z a^3+b^3=z
cnty = 0
cntx = 0
for z in range(1729, 100000):
    cnty = 0
    for x in range(100):
        for y in range(100):
            if x**3 + y**3 == z:
                cnty += 1
                if cnty == 4:
                    print(z)
                    cntx += 1
                if cntx == 5:
                    break
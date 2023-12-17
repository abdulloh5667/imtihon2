a = [1,2,3,4,5,7,8,9,10]
c = sorted(a)
for x in range(1,11):
    if x not in a:
        c.append(x)
        print(c)

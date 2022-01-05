p = [i for i in range(20, 51)]
q = [i for i in range(30, 41)]
a1 = [i for i in range(20, 31)]
a2 = [i for i in range(30, 41)]
a3 = [i for i in range(40, 51)]
a = [a1, a2, a3]
min = 100000000
for j in a:
    count = 0
    for x in range(0, 100):
        if (x in j) or not ((x in p) or (x in q)) == 1:
            count += 1
        else:
            count = 0
        print(count, (x in j) or not ((x in p) or (x in q)), x, j)
    if min > count:
        min = count
print(count)

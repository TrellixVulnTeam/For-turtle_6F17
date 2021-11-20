import time


start_time = time.time()

f = open('27-2a.txt', 'r')
aux = []
f.readline()
for i in f:
    aux.append(list(map(int, i.split())))
f.close()

max_para = [max(i) for i in aux]
summa = sum(max_para)
print(summa)

if summa % 3 == 0:
    print(summa)
else:
    delta = summa % 3
    min_division = max(max(aux))
    for i in aux:
        x = abs(i[0] - i[1])
        if x < min_division and x % 3 == delta:
            min_division = x
    print(summa - min_division)



print("--- %s seconds ---" % (time.time() - start_time))

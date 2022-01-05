file = open('26-59.txt', 'r')
aux = file.readline()
matrix = []
for string in file:
    matrix.append(tuple(map(int, string.split())))
file.close()

dic = dict.fromkeys(sorted(set([i[0] for i in matrix]), reverse=True))
for i in matrix:
    if dic[i[0]] == None:
        dic[i[0]] = [i[1]]
    else:
        dic[i[0]] = sorted(dic[i[0]] + [i[1]])

flag = False
for row, seats in dic.items():
    for i in range(len(seats) - 1):
        if seats[i + 1] - seats[i] == 3:
            print(row, seats[i] + 1)
            flag = True
            break
    if flag == True:
        break

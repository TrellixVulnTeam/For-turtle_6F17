file = open('26-57.txt', 'r')
aux, lenght = map(int, file.readline().split())
del aux
count = []
for line in file:
    count.append(int(line))
file.close()

count.sort(reverse=True)

slick = 0
while sum(count) >= lenght:
    aux_count = count.pop(0)
    if aux_count >= lenght:
        count.append(aux_count - lenght)
        count.sort(reverse=True)
    else:
        while aux_count + count[0] <= lenght:
            slick +=1
            aux_count += count.pop(0)
        for i in range(len(count)-1,-1,-1):
            if aux_count + count[i] >= lenght:
                slick += 1
                count.append(aux_count + count.pop(i) - lenght)
print(slick)
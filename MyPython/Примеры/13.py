#Удалить отрицательные элементы из списка
список=[1,-1,2,-2,3,-3,4,-4,-5]
cписок2=[]
print(список)
for i in список:
    if i > 0 :
        cписок2.append(i)

print(cписок2)


#Определить разницу в годах между самым старшим и младшим
from datetime import *
год=[]
ДР=(date(2012, 12, 14),date(2015, 2, 18),date(1812, 6, 28),date(2019, 5, 4))
др=list(ДР)
for i in ДР:
    год.append(i.year)
print("В годах ", max(год)-min(год))
print("В днях ", (max(др)-min(др)).days)

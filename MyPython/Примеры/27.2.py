a=[70,67,61,32,36,17,-1,-55]
print(a)
n=len(a)
k=0  #счётчик пар
q=15 #Кратность
o=[] #Массив где хранят колличество чисел с отатком равным номеру массива
for i in range(q):
    o.append(0)

for i in range(n):

    print(o,k)
    x=a[i]
    k+=o[(q-x%q)%q]
    o[x%q]+=1

print(o,k)
print(k)


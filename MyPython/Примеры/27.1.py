a=[10,100,45,55,245,35,25,10,10,10,26]
print(a)
i=0
n=len(a)
aux=[]
m=0
for i in range(n):
    aux.append(a[i])

for i in range(n-8):
    for j in range(i+8,n):
        m=max(a[i]*a[j],m)

print(m)



aux=[]
m=0
mp=0
for i in range(8):
    aux.append(a[i])

for i in range(8,n):

    if aux[0]>m:
        m=aux[0]

    for j in range (7):
        aux[j]=aux[j+1]

    aux[7]=a[i]

    if m*aux[7]>mp:
        mp=m*aux[7]
print(mp)


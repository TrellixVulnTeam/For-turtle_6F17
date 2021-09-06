j=0
a=[1,2,3,2,1,3]
print(a)
n=len(a)
for i in range(n-1):
    if  (a[i]*a[i+1])%3==0:
        j+=1

print(j)

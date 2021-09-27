
a=[1,5,4,1,5,8,4,2,1,3]
print(a)
n=len(a)
k=0
for i in range(n):
    k+=a[i]%2
#if k%2==0:
#    print(k)
#else:
#    print(num-k)

print(abs(n*(k%2)-k))    

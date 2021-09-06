п=1
e=float(input('Введите точность: '))
слагаемое =1
n=1
s = 1
while слагаемое > e:
   for i in range(1,n+1): s=s*i 
   слагаемое = 1/s
   п+=слагаемое
   n+=1
   s =1
print(п)

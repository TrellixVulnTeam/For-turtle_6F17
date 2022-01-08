def qqq():
    print("\n*******************************")
список=[1,2,3,4,5,6,7,8,9]
qqq()
for i in список:
    print(i)
qqq()
for i in range(1,len(список),2):
    print(i, end="")
qqq()
summ=0
for i in список:
    summ+=i
print(summ)

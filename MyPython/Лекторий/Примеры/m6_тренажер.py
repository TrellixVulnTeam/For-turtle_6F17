from random import *
er = 0
while 1==1:
    x = randint(2,10)
    b = randint(2,10)
    a = b*x
    print(a,' : ',b, end='')
    t=input(' = ')
    if t=='*': break
    else: n=int(t)
    if n != x: print('Ошибка'); er+=1
print('Количество ошибок: ',er)
print('Пока, пока!')

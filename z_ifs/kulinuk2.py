def if16(a, b, c):
    if a<b<c:
        a=a*2
        b=b*2
        c=c*2
        return(a,b,c)
    else:
        a=-a
        b=-b
        c=-c
        return(a,b,c)


def if17(a, b, c):
    if a>b>c or a<b<c:
        a=a*2
        b=b*2
        c=c*2
        return(a,b,c)
    else:
        a=-a
        b=-b
        c=-c
        return(a,b,c)


def if18(int1, int2, int3):
    if int1==int3  and int1!=int2:
        return(2)
    elif int1==int2  and int2!=int3:
        return(3)
    elif int2==int3 and int2!=int1:
        return(1)
    else:
        return('Неверные числа')


def if19(int1, int2, int3, int4 ):
    if int1==int3==int4  and int1!=int2:
        return(2)
    elif int1==int2==int4  and int2!=int3:
        return(3)
    elif int2==int3==int4 and int2!=int1:
        return(1)
    elif int1==int2==int3 and int1!=int4:
        return(4)
    else:
        return('Неверные числа')


def if20(a, b, c):
    if abs(a-c)>abs(a-b):
        return(b,abs(a-b))
    elif abs(a-b)>abs(a-c):
        return(c,abs(a-c))
    else:
        return('Неправильные числа')


def if21(int1, int2):
    if int1==int2==0:
        return(0)
    elif int1==0:
        return(1)
    elif int2==0:
        return(2)
    else:
        return(3)


def if22(float1, float2):
    if float1>0 and float2>0:
        return(1)
    elif float1<0 and float2>0:
        return(2)
    elif float1<0 and float2<0:
        return(3)
    elif float1>0 and float2<0:
        return(4)
    else:
        return('Точка лежит на границах четвертей')


def if23(int1,int1_2,int2,int2_2,int3,int3_2):
    int4 = int4_2 = None
    if int2==int3:
        int4=int1
    elif int3==int1:
        int4=int2
    elif int1==int2:
        int4=int3
    if int2_2==int3_2:
        int4_2=int1_2
    elif int3_2==int1_2:
        int4_2=int2_2
    elif int1_2==int2_2:
        int4_2=int3_2
    return(int4,int4_2)


import math
def if24(x):
    aux = None
    if x>0:
        fx=2*(math.sin(x))
        aux = fx
    elif x<=0:
        fx=6-x
        aux = fx
    return(aux)


import math
def if25(x):
    if x<-2 or x>2:
        fx=2*x
    else:
        fx=-3*x
    return(fx)

import math
def if26(x):
    if x<=0:
        fx=-x
    elif 0<x<2:
        fx=x**2
    elif x>=2:
        fx=4
    return(fx)


import math
def if27(x):
    if x<0:
        fx=0
    elif x%2==0:
        fx=1
    elif x%2!=0:
        fx=-1
    return(fx)


def if28(int1):
    a=0
    if int1%4==0:
        if int1%100==0 and int1%400!=0:
            a=365
        elif int1%100==0 and int1%400==0:
            a=366
        else:
            a=366
    else:
        a=365
    return(a)


def if29(int1):
    a=0
    b=0
    if int1<0:
        a='отрицательное '
    else:
        a='положительное '
        
        
    if int1%2==0 and int1!=0:
        b='четное '
    elif int1%2!=0 and int1!=0:
        b='нечетное '
    if int1==0:
        return('нулевое число')
    else:
        return(a + b + 'число')


def if30(int1):
    a=0
    b=0
    if int1//100<10 and int1//100!=0:
        a='трехзначное'
    elif int1//10<10 and int1//10!=0:
        a='двузначное'
    elif int1//10==0:
        a='однозначное'
        
    if int1%2==0 and int1!=0:
        b='четное '
    elif int1%2!=0 and int1!=0:
        b='нечетное '
    if 1<=int1<=999:
        return(a + b + 'число')
    else:
        return('Числе вне диапазона')


'''
Для проверки работы программ:
1. раскоментируйте нужную строку (удалите символ "#")
2. изменяя цифры в гументах функции проверте разные варианты решения задачи
3. если все работает как надо, можете сново закоментировать строку
'''
#if16(1, 2, 3)
#if17(1, 2, 3)
#if18(1, 2, 1)
#if19(1, 2, 3)
#if20(1, 2, 3)
#if21(1, 2)
#if22(1, 2)
#if23(1, 2, 3)
#if24(1)
#if25(1)
#if26(1)
#if27(1)
#if28(1)
#if29(1)
#if30(1)


def if16(a, b, c):
    if a<=b and b<=c:
        a=a*2
        b=b*2
        c=c*2
    else:
        a=a*(-1)
        b=b*(-1)
        c=c*(-1)
    return(a,b,c)


def if17(a, b, c):
    if (a<b and b<c) or (a>b and b>c):
        a=a*2
        b=b*2
        c=c*2
    else:
        a=a*(-1)
        b=b*(-1)
        c=c*(-1)
    return(a,b,c)



def if18(int1, int2, int3):
    if int1==int3:
        return(2)
    elif int2==int3:
        return(1)
    elif int1==int2:
        return(3)
    else:
        return('нет')



def if19(int1, int2, int3,int4):
    if int1==int3==int4:
        return(2)
    elif int2==int3==int4:
        return(1)
    elif int1==int2==int4:
        return(3)
    else:
        return(4)


def if20(a, b, c):
    if abs(a-b)<abs(a-c):
        return(b)
    elif abs(a-b)>abs(a-c):
        return(c)
    else:
        return('нет')


def if21(int1, int2):
    if int1==0 and  int2==0:
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
    elif float1>0 and float2<0:
        return(4)
    elif float1<0 and float2>0:
        return(2)
    else:
        return(3)



def if23(int1, int2, int3,int4,int5 ,int6):
    if int2==int3:
        x = int1
    elif int3==int1:
        x = int2
    else:
        x = int3

    if int4==int5:
        y =int4
    elif int6==int4:
        y = int5
    else:
        y = int6
    return x, y

import math
def if24(x):

    if x>0:
        return(2*math.sin(x))
    else:
        return(6-x)


def if25(x):
    if (x<-2) or (x>2):
        return(2*x)
    else:
        return(-3*x)


def if26(x):
    if x<=0:
        return(-x)
    elif (0<x) and (x<2):
        return(x*x)
    else:
        return(4)


def if27(x):
    if (x<0):
        return(0)
    elif x%2==0:
        return(1)
    else:
        return(-1)


def if28(int):
    if int%100==0:
       if int%400==0:
            return(366)
       else:
           return(365)
    elif int%4==0:
        return(366)
    else:
        return(365)


def if29(int):
    if int==0:
        return('нулевое' )
    elif int>0 and int%2== 0:
        return('положительное четное ')
    elif int>0 and int%2== 1:
        return('отрицательное нечетное')
    elif int<0 and int%2== 0:
        return('отрицательное четное ')
    elif int<0 and int%2== 1 :
        return('отрицательное нечетное ')



def if30(int):
    if int%2==0:
        return("четное ")
    elif int%2==0 :
        return("нечетное ")
    elif int>99:
        return("трехзначное ")
    elif 99>=int and int > 9:
        return("двухзначное ")
    elif int<= 9:
        return("однозначное ")
    else:
        return('нечетное трехзначное')


'''
Для проверки работы программ:
1. раскоментируйте нужную строку (удалите символ "#")
2. изменяя цифры в гументах функции проверте разные варианты решения задачи
3. если всё работает как надо, можете сново закоментировать строку
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

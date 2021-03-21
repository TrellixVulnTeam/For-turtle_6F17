def if16(a,b,c):
    if (a<b) and (b<c):
        a=a*2
        b=b*2
        c=c*2
        return(a,b,c)
    else:
        a=-a
        b=-b
        c=-c
        return(a,b,c)


def if17(a,b,c):
    if ((a<b) and (b<c))or((a>b)and(b>c)):
        a=a*2
        b=b*2
        c=c*2
        return(a,b,c)
    else:
        a=-a
        b=-b
        c=-c
        return(a,b,c)


def if18(int1,int2,int3):
    if int3==int2:
        return(1)
    elif int1==int3:
        return(2)
    else:
        return(3)



def if19(int1,int2,int3,int4):
    if (int3==int2)and (int3==int4):
        return(1)
    elif (int1==int3)and (int3==int4):
        return(2)
    elif (int1==int2) and(int2==int4):
        return(3)
    else:
        return(4)



def if20(a,b,c):
    if abs(a-b)<abs(a-c):
        return(b,abs(a-b))
    else:
        return(c,abs(a-c))


def if21(int1,int2):
    if (int1==0) and (int2==0):
        return(0)
    elif (int1==0) and (int2!=0):
        return(1)
    elif (int1!=0) and (int2==0):
        return(2)
    else:
        return(3)


def if22(float1, float2):
    if (float1>0) and (float2>0):
        return(1)
    elif (float1<0) and (float2>0):
        return(2)
    elif (float1<0) and (float2<0):
        return(3)
    else:
        return(4)

def if23(int1,int2,int3,int4,int5,int6):
    if int2==int3 :
       x4=int1
    elif int3==int1 :
        x4=int2
    else:
        x4=int3
    if int5==int6:
        y4=int4
    elif int6==int4:
        y4=int5
    else:
        y4=int6
    return x4, y4


import math
def if24(x):
    if x>0:
        return(2*math.sin(x))
    else:
        return(6-x)



def if25(x):
    if x<(-2) or x>2:
        return(2*x)
    else:
        return((-3)*x)



def if26(x):
    if x<=0:
        return((-1)*x)
    elif (0<x) and (x<2):
        return(x**2)
    elif x>=2:
        return(4)


def if27(x):
    if x<0:
        return(0)
    elif (x%2)==0 :
        return(1)
    elif (x%2)!=0:
        return(-1)


def if28(int):
    if (int % 4 == 0) and ((int % 100 != 0) or (int % 400 == 0)):
        return(366)
    else:
        return(365)


def if29(int):
    if int==0:
        a="нулевое "
    if int>0:
        a="положительное "
    else:
        a="отрицательное "
    if int%2==0:
        a += "четное"
    else:
        a += "нечетное"

    return a



def if30(int):
    if (int % 2) == 0 :
        a = 'чётное '
    else:
        a = 'нечётное '

    if int> 99 :
        a += 'трёхзначное '
    if (99 >=int) and (int > 9) :
        a += 'двухзначное '
    if int<= 9  :
        a += 'однозначное '
    return a



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

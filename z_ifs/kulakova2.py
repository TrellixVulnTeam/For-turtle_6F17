def if16(a, b, c):
    """
    If16. Даны три переменные вещественного типа: a, b, c.
    Если их значения упорядочены по возрастанию, то удвоить их;
    в противном случае заменить значение каждой переменной на противоположное.
    Вывести новые значения переменных a, b, c.
    """
    if a<b<c:
        return(a*2,b*2,c*2)
    else:
        return(a*-1,b*-1,c*-1)
      


def if17(a, b, c):
    """
    If17. Даны три переменные вещественного типа: a, b, c.
    Если их значения упорядочены по возрастанию или убыванию, то удвоить их;
    в противном случае заменить значение каждой переменной на противоположное.
    Вывести новые значения переменных a, b, c.
    """
    if a<b<c or a>b>c:
        return(a*2,b*2,c*2)
    else:
        return(a*-1,b*-1,c*-1)


def if18(int1, int2, int3):
    """
    If18. Даны три целых числа, одно из которых отлично от двух других, равных между собой.
    Определить порядковый номер числа, отличного от остальных.
    """
    if int2==int3:
        return(1)
    elif int1==int3:
        return(2)
    elif int1==int2:
        return(3)
    else:
        return("все числа различны")


def if19(int1, int2, int3,int4):
    """
    If19. Даны четыре целых числа, одно из которых отлично от трех других, равных между собой.
    Определить порядковый номер числа, отличного от остальных.
    """
    if int2==int3==int4:
        return(1)
    elif int1==int3==int4:
        return(2)
    elif int1==int2==int4:
        return(3)
    elif int1==int2==int3:
        return(4)
    else:
        return("нет трех одинаковых чисел")

def if20(a, b, c):
    """
    If20. На числовой оси расположены три точки: a, b, c.
    Определить, какая из двух последних точек (b или c) расположена ближе к a,
    и вывести эту точку и ее расстояние от точки a.
    """
    if abs(a-c)<abs(a-b):
        return(c, (abs(a-c)))
    elif abs(a-c)>abs(a-b):
        return(b, abs(a-b))
    else:
        return("точка находиться на одинаковом расстоянии") 

def if21(int1, int2):
    """
    If21. Даны целочисленные координаты точки на плоскости.
    Если точка совпадает с началом координат, то вывести 0.
    Если точка не совпадает с началом координат, но лежит на оси OX или OY, то вывести соответственно 1 или 2.
    Если точка не лежит на координатных осях, то вывести 3.
    """
    if int1==int2==0:
        return(0)
    elif int1==0:
        return(1)
    elif int2==0:
        return(2)  
    else:
        return(3) 


def if22(float1, float2):
    """
    If22. Даны координаты точки, не лежащей на координатных осях OX и OY.
    Определить номер координатной четверти, в которой находится данная точка.
    """
    if float1>0 and float2>0:
        return(1)
    elif float1>0 and float2<0:
        return(4)
    elif float1<0 and float2<0:
        return(3)
    elif float1<0 and float2>0:
        return(2)
    else:
        return("невозможно определить четверть")


def if23(int1, int2, int3, int4, int5, int6):
    """
    If23. Даны целочисленные координаты трех вершин прямоугольника,
    стороны которого параллельны координатным осям. Найти координаты его четвертой вершины.
    """
    return(int2, int3)

def if24(x):
    """
    If24. Для данного вещественного x найти значение следующей функции f,
    принимающей вещественные значения:f(x)=2∙sin(x),если x >0 и 6-x,если x ≤0
    """
    import math
    if x>0:
        return(2*math.sin(x))
    else:
        return(6-x)


def if25(x):
    """
    If25. Для данного целого x найти значение следующей функции f,
    принимающей значения целого типа:f(x)=2∙x ,если x<-2 или x>2, и -3∙x,в противном случае
    """
    if x<-2 or x>2:
        return(2*x)
    else:
        return(-3*x)


def if26(x):
    """
    If26. Для данного вещественного x найти значение следующей функции f,
    принимающей вещественные значения:f(x)=-x,если x ≤0, и x^2,если 0<x<2 и 4,если x ≥2
    """
    if x<=0:
        return(-1*x)
    elif 0<x<2:
        return(x*x)
    elif x>=2:
        return(4)


def if27(x):
    """
    If27. Для данного вещественного x найти значение следующей функции f,
    принимающей значения целого типа:    
    if x<=0:f(x)=0,если x<0, и 1,если x принадлежит [0,1),[2,3),…,
    и -1,если x принадлежит [1,2),[3,4),….)"""
    if x<=0:
        return(0)
    elif x%2==1:
        return(-1)
    elif x%2==0:
        return(1)


def if28(int):
    """
    If28. Дан номер года (положительное целое число).
    Определить количество дней в этом году, учитывая, что обычный год насчитывает 365 дней, \
    а високосный - 366 дней. Високосным считается год, делящийся на 4,
    за исключением тех годов, которые делятся на 100 и не делятся на 400
    (например, годы 300, 1300 и 1900 не являются високосными, а 1200 и 2000 - являются).
    """
    if int%4==0 and int%100==0 and int%400==0:
        return(366)
    else:
        return(365)


def if29(int):
    """
    If29. Дано целое число. Вывести его строку-описание вида «отрицательное четное число»,
    «нулевое число», «положительное нечетное число» и т. д.
    """
    if int==0:
        return ("нулевое число")
    elif int>0 and int%2==0:
        return("положительное четное число")
    elif int>0 and int%2==1:
        return("положительное нечетное число")        
    elif int<0 and int%2==0:
        return("отрицательное четное число")
    elif int<0 and int%2==1:
        return("отрицательное нечетное число")


def if30(int):
    """
    If30. Дано целое число, лежащее в диапазоне 1–999.
    Вывести его строку-описание вида «четное двузначное число», «нечетное трехзначное число» и т. д.
    """
    if int%2==1 and 0<=int<10:
        return("нечетное однозначное число")
    elif int%2==1 and 10<=int<=99:
        return("нечетное двузначное число")
    elif int%2==1 and 100<=int<=999:
        return("нечетное трехзначное число")
    elif int%2==0 and 0<=int<10:
        return("четное однозначное число")
    elif int%2==0 and 10<=int<=99:
        return("четное двузначное число")
    else:
        return("нечетное трехзначное число")


'''
Для проверки работы программ:
1. раскоментируйте нужную строку (удалите символ "#")
2. изменяя цифры в гументах функции проверте разные варианты решения задачи
3. если все работает как надо, можете сново закоментировать строку
'''
#if16(11, 7, 3)
#if17(9, 5, 2)
#if18(1, 2, 1)
#if19(1, 2, 3, 5)
#if20(1, 2, 3)
#if21(1, 2)
#if22(1, 2)
#if23(1, 2, 3)
#if24(4)
#if25(1)
#if26(1)
#if27(34)
#if28(1)
#if29(-4)
#if30(15)
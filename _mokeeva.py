def if1(int_number):
    """
    If1.Дано целое число. Если оно является положительным, то вычесть из него 8;
    в про-тивном случае не изменять его. Вывести полученное число.
    """
    if int_number>0:
       int_number-=8
       return(int_number)
    else:
        return(int_number)

def if2(int_number):
    """
    If2. Дано целое число. Если оно является положительным, то вычесть из него 8;
    в про-тивном случае прибавить к нему 6. Вывести полученное число.
    """
    if int_number>0:
       int_number-=8
       return(int_number)
    else:
       int_number+=6 
       return(int_number)


def if3(int_number):
    """
    If3. Дано целое число. Если оно является положительным, то вычесть из него 8;
    если отрицательным, то прибавить к нему 6; если нулевым, то заменить его на 10.
    Вывести полученное число.
    """
    if int_number>0:
       int_number-=8
    else:
       int_number+=6

    if int_number==0:
       int_number=10

    return(int_number)

def if4(int1, int2, int3):
    """
    If4. Даны три целых числа. Найти количество положительных чисел в исходном наборе.
    """
    a = 0
    if int1>0:
        a+= 1
    if int2>0:
        a+= 1
    if int3>0:
        a+= 1
    return(a)


def if5(int1, int2, int3):

    """
    If5. Даны три целых числа. Найти количество положительных
    и количество отрица-тельных чисел в исходном наборе.
    """
    a=0
    if int1>0:
        a+=1
    if int2>0:
        a+=1
    if int3>0:
        a+=1
    a1=0
    if int1<0:
        a1+=1
    if int2<0:
        a1+=1
    if int3<0:
        a1+=1
    return(a, a1)

def if6(int1, int2):

    """
    If6. Даны два числа. Вывести большее из них.
    """
    if int1>int2:
        return(int1)
    else:
        return(int2)
    

def if7(int1, int2):

    """
    If7. Даны два числа. Вывести порядковый номер меньшего из них.
    """
    if int1<int2:
        return(int1)
    else:
        return(int2)


def if8(int1, int2):

    """
    If8. Даны два числа. Вывести вначале большее, а затем меньшее из них.
    """
    if int1>int2:
        return(int1,int2)
    else:
        return(int2,int1)


def if9(a, b):
    """
    If9. Даны две переменные вещественного типа: a, b.
    Перераспределить значения дан-ных переменных так, чтобы в a оказалось меньшее из значений,
    а в b - большее. Вывести новые значения переменных a и b.
    """
    a,b=(min(a,b),max(a,b))
    return(a, b)


def if10(a, b):
    """
    If10. Даны две переменные целого типа: a и b.
    Если их значения не равны, то присвоить каждой переменной сумму этих значений,
    а если равны, то присвоить переменным нулевые значения.
    Вывести новые значения переменных a и b.
    """
    if a!=b:
        return(a)
    else:
        return(b)


def if11(a, b):
    """
    If11. Даны две переменные целого типа: a и b.
    Если их значения не равны, то присвоить каждой переменной большее из этих значений,
    а если равны, то присвоить пере-менным нулевые значения. Вывести новые значения переменных a и b.
    """
    pass



def if12(int1, int2, int3):
    """
    If12. Даны три числа. Найти наименьшее из них.
    """
    if int2>=int1<=int3:
        return(int1)
    elif int1>=int2<=int3:
        return(int2)
    else:
        return(int3)


def if13(float1, float2, float3):
    """
    If13. Даны три числа. Найти среднее из них (т.е. число, расположенное между наименьшим и наибольшим).
    """
    if float2<float3<float3 or float3<float1<float2:
        return('Среднее',float1)
    elif float1<float2<float3 or float3<float2<float1:
        return('Среднее',float1)
    else:
        return('Среднее',float3)


def if14(float1, float2, float3):
    """
    If14. Даны три числа. Вывести вначале наименьшее, а затем наибольшее из данных чисел.
    """
    if float1<float2:
        return(float1,float2)
    elif float2<float3:
        return(float2,float3)
    else:
        return(float3,float2)


def if15(float1, float2, float3):
    """
    If15. Даны три числа. Найти сумму двух наибольших из них.
    """
    if float1<float2:
        min=float1
    else:
        min=float2
    if float3<min:
        min=float3

    summ = float1+float2+float3-min
    return("Сумма двух  наибольших =",summ)

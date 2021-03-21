def if1(int_number):
    """
    If1.Дано целое число. Если оно является положительным, то вычесть из него 8;
    в про-тивном случае не изменять его. Вывести полученное число.
    """
    if int_number>0:
        int_number-=8
    return int_number


def if2(int_number):
    """
    If2. Дано целое число. Если оно является положительным, то вычесть из него 8;
    в про-тивном случае прибавить к нему 6. Вывести полученное число.
    """
    if int_number>0:
        int_number-=8
    else:
        int_number+=6
    return int_number


def if3(int_number):
    """
    If3. Дано целое число. Если оно является положительным, то вычесть из него 8;
    если отрицательным, то прибавить к нему 6; если нулевым, то заменить его на 10.
    Вывести полученное число.
    """
    if int_number>0:
        int_number-=8
    elif int_number==0:
        int_number=10
    else:
        int_number+=6
    return int_number


def if4(int1, int2, int3):
    """
    If4. Даны три целых числа. Найти количество положительных чисел в исходном наборе.
    """
    N=0
    if int1>0:
        N+=1
    if int2>0:
        N+=1
    if int3>0:
        N+=1
    return N


def if5(int1, int2, int3):

    """
    If5. Даны три целых числа. Найти количество положительных
    и количество отрица-тельных чисел в исходном наборе.
    """
    N=0
    F=0
    if int1>0:
        N+=1
    else:
        F+=1
    if int2>0:
        N+=1
    else:
        F+=1
    if int3>0:
        N+=1
    else:
        F+=1
    return N, F


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
       return 1
    else:
       return 2


def if8(int1, int2):

    """
    If8. Даны два числа. Вывести вначале большее, а затем меньшее из них.
    """

    if int1>int2:
        return int1,int2
    else:
        return int2,int1

def if9(a, b):
    """
    If9. Даны две переменные вещественного типа: a, b.
    Перераспределить значения дан-ных переменных так, чтобы в a оказалось меньшее из значений,
    а в b - большее. Вывести новые значения переменных a и b.
    """
    if a>b:
        n=a
        a=b
        b=n
    return a, b


def if10(a, b):
    """
    If10. Даны две переменные целого типа: a и b.
    Если их значения не равны, то присвоить каждой переменной сумму этих значений,
    а если равны, то присвоить переменным нулевые значения.
    Вывести новые значения переменных a и b.
    """
    if a!=b:
        n=a
        a=a+b
        b=n+b
    else:
        a=0
        b=0
    return a, b


def if11(a, b):
    """
    If11. Даны две переменные целого типа: a и b.
    Если их значения не равны, то присвоить каждой переменной большее из этих значений,
    а если равны, то присвоить пере-менным нулевые значения. Вывести новые значения переменных a и b.
    """
    if a!=b and a>b: 
        b=a 
    elif a!=b and b>a: 
        a=b 
    else: 
        a=0 
        b=0 
    return a, b



def if12(int1, int2, int3):
    """
    If12. Даны три числа. Найти наименьшее из них.
    """
    if int1<int2: 
        if int1<int2: 
            return(int1) 
        else: 
            return(int3) 
    else: 
        if int2<int3: 
            return(int2) 
        else: 
            return(int3)


def if13(float1, float2, float3):
    """
    If13. Даны три числа. Найти среднее из них (т.е. число, расположенное между наименьшим и наибольшим).
    """
    if float1<=float2<=float3 or float3<=float2<=float1: 
        return(float2) 
    elif float2<=float1<=float3 or float3<=float1<=float2: 
        return(float1) 
    else: 
        return(float3)


def if14(float1, float2, float3):
    """
    If14. Даны три числа. Вывести вначале наименьшее, а затем наибольшее из данных чисел.
    """
    min1=float1 
    max1=float1 
    if min1>float2: 
        min1=float2 
    else: 
        if max1<float2: 
            max1=float2 
    if min1>float3: 
        min1=float3 
    else: 
        if max1<float3: 
            max1=float3 
    return(min1, max1)


def if15(float1, float2, float3):
    """
    If15. Даны три числа. Найти сумму двух наибольших из них.
    """
    if float2>=float1<=float3 or float3>=float1<=float2:
        return(float2+float3)
    elif float1>=float2<=float3 or float3>=float2<=float1:
        return(float1+float3)
    else:
        return(float1+float2)

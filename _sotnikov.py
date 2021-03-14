def if1(int_number):
    """
    If1.Дано целое число. Если оно является положительным, то вычесть из него 8;
    в про-тивном случае не изменять его. Вывести полученное число.
    """
    if int_number>0:
        int_number-=8
    return(int_number)

def if2(int_number):
    """
    If2. Дано целое число. Если оно является положительным, то вычесть из него 8;
    в про-тивном случае прибавить к нему 6. Вывести полученное число.
    """
    if int_number>0:
        int_number-=8
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
    elif int_number<0:
        int_number+=6
    else:
        int_number=10
    return(int_number)

def if4(int1, int2, int3):
    """
    If4. Даны три целых числа. Найти количество положительных чисел в исходном наборе.
    """
    a=0
    if int1>0:
       a+=1
    if int2>0:
        a+=1
    if int3>0:
        a+=1
    return(a)


def if5(int1, int2, int3):

    """
    If5. Даны три целых числа. Найти количество положительных
    и количество отрица-тельных чисел в исходном наборе.
    """
    a=0
    if  int1>0:
       a+=1
    if int2>0:
        a+=1
    if int3>0:
        a+=1
    b=0
    if  int1<0:
       b+=1
    if int2<0:
        b+=1
    if int3<0:
        b+=1
    return(a, b)


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
    if int1>int2:
        a=1
    else:
        a=2
    return(a)




def if8(int1, int2):

    """
    If8. Даны два числа. Вывести вначале большее, а затем меньшее из них.
    """
    if  int1>int2:
        return(int1,int2)
    else:
        return(int2,int1)

    
def if9(a, b):
    """
    If9. Даны две переменные вещественного типа: a, b.
    Перераспределить значения дан-ных переменных так, чтобы в a оказалось меньшее из значений,
    а в b - большее. Вывести новые значения переменных a и b.
    """
    if a>b:
        a,b=b,a
    return(a,b)
   

def if10(a, b):
    """
    If10. Даны две переменные целого типа: a и b.
    Если их значения не равны, то присвоить каждой переменной сумму этих значений,
    а если равны, то присвоить переменным нулевые значения.
    Вывести новые значения переменных a и b.
    """
    if a!=b:
        a=b=a+b
    else:
        a=b=0
    return(a,b)



def if11(a, b):
    """
    If11. Даны две переменные целого типа: a и b.
    Если их значения не равны, то присвоить каждой переменной большее из этих значений,
    а если равны, то присвоить пере-менным нулевые значения. Вывести новые значения переменных a и b.
    """
    if a!=b:
        a=b=max(a,b)
    else:
        a=b=0
    return(a,b)
    
  

def if12(int1, int2,int3):
    """
    If12. Даны три числа. Найти наименьшее из них.
    """
    if int1<int2:
        a=int1
    else:
        a=int2
    if  a>int3:
        a=int3
    return(a)
    
        


def if13(float1, float2, float3):
    """
    If13. Даны три числа. Найти среднее из них (т.е. число, расположенное между наименьшим и наибольшим).
    """
    x = float1
    y = float2
    z = float3
    if (x<=y and y<=z) or (z<=y and y<=x):
        a=y
    elif (y<=x and x<=z) or (z<=x and  x<=y):
        a=x
    elif (x<=z and z<=y) or (y<=z and z<=x):
        a=z
    return(a)


def if14(float1, float2, float3):
    """
    If14. Даны три числа. Вывести вначале наименьшее, а затем наибольшее из данных чисел.
    """
    x = float1
    y = float2
    z = float3
    if x>y:
        a=y
        b=x
    else:
        a=x
        b=y
    if b<z:
        b=z
    if a>z:
        a=z
    return(a,b)



def if15(float1, float2, float3):
    """
    If15. Даны три числа. Найти сумму двух наибольших из них.
    """
    x = float1
    y = float2
    z = float3
    if (z<=x and x<=y) or (z<=y and y<=x):
        a=x+y
    elif (y<=x and x<=z) or (y<=z and z<=x):
        a=x+z
    elif (x<=z and z<=y) or (x<=y and y<=z):
        a=y+z
    return(a)

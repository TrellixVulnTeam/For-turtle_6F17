def if1(int_number):
    """
    If1.Дано целое число. Если оно является положительным, то вычесть из него 8;
    в про-тивном случае не изменять его. Вывести полученное число.
    """
    if int_number > 0:
        int_number -= 8
        return (int_number)
    else:
        return(int_number)



def if2(int_number):
    """
    If2. Дано целое число. Если оно является положительным, то вычесть из него 8;
    в про-тивном случае прибавить к нему 6. Вывести полученное число.
    """
    if int_number > 0:
        int_number -= 8
        return(int_number)
    else:
        int_number+= 6
        return(int_number)


def if3(int_number):
    """
    If3. Дано целое число. Если оно является положительным, то вычесть из него 8;
    если отрицательным, то прибавить к нему 6; если нулевым, то заменить его на 10.
    Вывести полученное число.
    """
    if int_number == 0:
      return(10)
    elif int_number > 0:
        int_number -= 8
        return(int_number)
    else:
        int_number+= 6
        return(int_number)



def if4(int1, int2, int3):
    """
    If4. Даны три целых числа. Найти количество положительных чисел в исходном наборе.
    """
    if int1<0 and int2<0 and int3<0:
        return(0)
    elif int1==0 and int2==0 and int3==0:
        return(0) 
    elif int1>0 and int2>0 and int3>0:
        return(3)
    elif (int1>0 and int2<0 and int3<0)or(int1<0 and int2>0 and int3<0)or(int1<0 and int2<0 and int3>0):
        return(1)
    else:
        return(2)


def if5(int1, int2, int3):

    """
    If5. Даны три целых числа. Найти количество положительных
    и количество отрица-тельных чисел в исходном наборе.
    """
    if int1<0 and int2<0 and int3<0:
        return(0,3)
    elif int1==0 and int2==0 and int3==0:
        return(0,0)
    elif int1>0 and int2>0 and int3>0:
        return(3,0)
    elif (int1>0 and int2<0 and int3<0)or(int1<0 and int2>0 and int3<0)or(int1<0 and int2<0 and int3>0):
        return(1,2)
    else:
        return(2,3)


def if6(int1, int2):

    """
    If6. Даны два числа. Вывести большее из них.
    """
    return(max(int1, int2))



def if7(int1, int2):

    """
    If7. Даны два числа. Вывести порядковый номер меньшего из них.
    """
    if int1>int2:
        return(1)
    elif int1<int2:
        return(2)
    else:
        return(2)


def if8(int1, int2):

    """
    If8. Даны два числа. Вывести вначале большее, а затем меньшее из них.
    """
    if int1>int2:
        return(int1,int2)
    elif int1<int2:
        return(int2,int1)
    else:
        return(int2,int1)


def if9(a, b):
    """
    If9. Даны две переменные вещественного типа: a, b.
    Перераспределить значения дан-ных переменных так, чтобы в a оказалось меньшее из значений,
    а в b - большее. Вывести новые значения переменных a и b.
    """
    a=(min(a,b))
    b=(max(a,b))
    return(a,b)


def if10(a, b):
    """
    If10. Даны две переменные целого типа: a и b.
    Если их значения не равны, то присвоить каждой переменной сумму этих значений,
    а если равны, то присвоить переменным нулевые значения.
    Вывести новые значения переменных a и b.
    """
    if a!=b:
        a,b=(a+b),(a+b)
        return(a,b)
    else:
        a,b=0,0
        return(a,b)
  


def if11(a, b):
    """
    If11. Даны две переменные целого типа: a и b.
    Если их значения не равны, то присвоить каждой переменной большее из этих значений,
    а если равны, то присвоить пере-менным нулевые значения. Вывести новые значения переменных a и b.
    """
    if a!=b:
        a=(max(a,b))
        b=(max(a,b))
        return(a,b)
    else:
        a,b=0,0
        return(a,b)
  


def if12(int1, int2, int3):
    """
    If12. Даны три числа. Найти наименьшее из них.
    """
    return(min(int1, int2, int3))
  


def if13(float1, float2, float3):
    """
    If13. Даны три числа. Найти среднее из них (т.е. число, расположенное между наименьшим и наибольшим).
    """
    return((float1+float2+float3)-(max(float1, float2, float3))-(min(float1, float2, float3)))


def if14(float1, float2, float3):
    """
    If14. Даны три числа. Вывести вначале наименьшее, а затем наибольшее из данных чисел.
    """
    return(min(float1, float2, float3), max(float1, float2, float3))


def if15(float1, float2, float3):
    """
    If15. Даны три числа. Найти сумму двух наибольших из них.
    """
    return((float1+float2+float3)-(min(float1, float2, float3)))
  
  #if1(3)
  #if2(0)
  #if3(6)
  #if4(-3,-5,3)
  #if5(8,9,-4)
  #if6(6,7)
  #if7(9,-13)
  #if8(12,-2)
  #if9(4,5)
  #if10(0,-2)
  #if11(7,-8)
  #if12(-3,3)
  #if13(4,0,-2)
  #if14(0,5,-2)
  #if15(0,9,-3)
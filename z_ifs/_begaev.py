def if1(int_number):
    """
    If1.Дано целое число. Если оно является положительным, то вычесть из него 8;
    в про-тивном случае не изменять его. Вывести полученное число.
    """
    if int_number > 0:
        int_number -= 8
    return int_number
def if2(int_number):
    """
    If2. Дано целое число. Если оно является положительным, то вычесть из него 8;
    в про-тивном случае прибавить к нему 6. Вывести полученное число.
    """
    if int_number > 0:
        int_number -= 8
    else:
        int_number += 6
    return int_number
def if3(int_number):
    """
    If3. Дано целое число. Если оно является положительным, то вычесть из него 8;
    если отрицательным, то прибавить к нему 6; если нулевым, то заменить его на 10.
    Вывести полученное число.
    """
    if int_number > 0:
        int_number -= 8
    elif int_number < 0:
        int_number += 6
    else:
        int_number = 10
    return int_number
def if4(int1, int2, int3):
    """
    If4. Даны три целых числа. Найти количество положительных чисел в исходном наборе.
    """
    a = 0
    if int1 > 0:
        a += 1
    if int2 > 0:
        a += 1
    if int3 > 0:
        a += 1
    return a
def if5(int1, int2, int3):
    """
    If5. Даны три целых числа. Найти количество положительных
    и количество отрица-тельных чисел в исходном наборе.
    """
    b = 0
    a = 0
    if int1 > 0:
        a += 1
    else:
        b += 1
    if int2 > 0:
        a += 1
    else:
        b += 1
    if int3 > 0:
        a += 1
    else:
        b += 1
    return a, b
def if6(int1, int2):
    """
    If6. Даны два числа. Вывести большее из них.
    """
    M = max(int1, int2)
    return M
def if7(int1, int2):
    """
    If7. Даны два числа. Вывести порядковый номер меньшего из них.
    """
    a = 0
    if int1 < int2:
        a = 1
    else:
        a = 2
    return a
def if8(int1, int2):
    """
    If8. Даны два числа. Вывести вначале большее, а затем меньшее из них.
    """
    if int1 < int2:
        return int2, int1
    else:
        return int1, int2
def if9(a, b):
    """
    If9. Даны две переменные вещественного типа: a, b.
    Перераспределить значения дан-ных переменных так, чтобы в a оказалось меньшее из значений,
    а в b - большее. Вывести новые значения переменных a и b.
    """
    if a > b:
        a, b = b, a
    return a, b
def if10(a, b):
    """
    If10. Даны две переменные целого типа: a и b.
    Если их значения не равны, то присвоить каждой переменной сумму этих значений,
    а если равны, то присвоить переменным нулевые значения.
    Вывести новые значения переменных a и b.
    """
    if a != b:
        a += b
        b = a
    else:
        a = 0
        b = 0
    return a, b
def if11(a, b):
    """
    If11. Даны две переменные целого типа: a и b.
    Если их значения не равны, то присвоить каждой переменной большее из этих значений,
    а если равны, то присвоить пере-менным нулевые значения. Вывести новые значения переменных a и b.
    """
    if a != b:
        a = max(a, b)
        b = max(a, b)
    else:
        a = 0
        b = 0
    return a, b
def if12(float1, float2, float3):
    """
    If12. Даны три числа. Найти наименьшее из них.
    """
    m = False

    if (float1 > float2) and (float3 > float2):
        m = float2
    if (float1 > float3) and (float2 > float3):
        m = float3
    if (float2 > float1) and (float3 > float1):
        m = float1

    return m
def if13(float1, float2, float3):
    """
    If13. Даны три числа. Найти среднее из них (т.е. число, расположенное между наименьшим и наибольшим).
    """
    if ((float1 >= float2) and (float3 <= float2)) or ((float1 <= float2) and (float3 >= float2)):
        a = float2
    if ((float1 >= float3) and (float2 <= float3)) or ((float1 <= float3) and (float2 >= float3)):
        a = float3
    if ((float2 >= float1) and (float3 <= float1)) or ((float2 <= float1) and (float3 >= float1)):
        a = float1
    return a
def if14(float1, float2, float3):
    """
    If14. Даны три числа. Вывести вначале наименьшее, а затем наибольшее из данных чисел.
    """
    m = float2
    if (float1 > float2) and (float3 > float2):
        m = float2
    if (float1 > float3) and (float2 > float3):
        m = float3
    if (float2 > float1) and (float3 > float1):
        m = float1

    return m, max(float1, float2, float3)
def if15(float1, float2, float3):
    """
    If15. Даны три числа. Найти сумму двух наибольших из них.
    """
    if (float1 <= float2) and (float1 <= float3):
        a = float2 + float3
    if (float2 <= float1) and (float2 <= float3):
        a = float1 + float3
    if (float3 <= float1) and (float3 <= float2):
        a = float1 + float2
    return a


'''
Для проверки работы программ:
1. раскоментируйте нужную строку (удалите символ "#")
2. изменяя цифры в гументах функции проверте разные варианты решения задачи
3. если всё работает как надо, можете сново закоментировать строку
'''
# if1(1)
# if2(1)
# if3(1)
# if4(1, 2, 3)
# if5(-1, 2, 3)
# if6(1, 2)
# if7(1, 2)
# if8(1, 2)
# if9(1, 2)
# if10(1, 2)
# if11(1, 2)
# if12(1, 2, 3)
# if13(2, 2, 3)
# if14(1, 2, 3)
# if15(2, 2, 2)

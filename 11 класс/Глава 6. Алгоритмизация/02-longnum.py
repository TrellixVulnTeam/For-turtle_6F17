# -*- coding: utf-8 -*-
"""
 Программа к учебнику информатики для 11 класса
 К.Ю. Полякова и Е.А. Еремина.
 Глава 6.
 Программа № 2. Длинные числа (факториал 100) 
 Вход: 
   нет 
 Результат: 
   Факториал числа 100:
   93326215443944152681...
"""
d = 1000000  # Основание системы счисления
A = [1]  # 0!
for k in range(2, 101):  # Умножение на числа от 2 до 100
    r = 0  # Перенос на следующий порядок
    for i in range(len(A)):  # Запись длинного числа длинного числа
        s = A[i] * k + r  # умножение разряда i на число k
        A[i] = s % d  # запись значения в разряд числа
        r = s // d  # определние переноса на следующий разряд
    if r > 0:
        A.append(r)  # Создание следующего разряда, если в этом есть необходимость

h = len(A) - 1
print(A[h], end="")
for i in range(h - 1, -1, -1):  # Печать "длинного" числа
    print(f"{A[i]:06d}", end="")  # форматирование числа с дописыванием нулей

print("\n")
A = 1
for k in range(2, 101):  # Вычисление 100! в Python
    A = A * k
print(A)  # Печать результата вычисления 100!

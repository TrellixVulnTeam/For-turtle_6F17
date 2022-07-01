# -*- coding: utf-8 -*-
"""
 Программа к учебнику информатики для 10 класса
 К.Ю. Полякова и Е.А. Еремина.
 Глава 8.
 Программа № 38. Поиск максимума в массиве
 Вход: 
   1 2 8 4 5
 Результат:
   Максимум: A[3]=8
   Максимум: A[3]=8
"""
print ( "Введите элементы массива:" )
A = list( map(int, input().split()) )
N = len(A)  

nMax = 0
for i in range(1,N):
  if A[i] > A[nMax]:
    nMax = i
print ( "Максимум: A[", nMax, "]=", A[nMax], sep="" )  

M = max(A)
nMax = A.index(M)
print ( "Максимум: A[", nMax, "]=", M, sep = "" );


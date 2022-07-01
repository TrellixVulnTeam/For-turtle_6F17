# -*- coding: utf-8 -*-
"""
 Программа к учебнику информатики для 10 класса
 К.Ю. Полякова и Е.А. Еремина.
 Глава 8.
 Программа № 36. Линейный поиск в массиве с break
 Вход: 
   1 2 3 4 5
   3
 Результат:
   A[2]=3
   A[2]=3
   A[2]=3
"""
print ( "Введите элементы массива:" )
A = list( map(int, input().split()) )
N = len(A)

print ( "Что ищем? " ) 
X = int(input())

nX = -1
for i in range(N):
  if A[i] == X: 
    nX = i
    break
  i += 1
if nX >= 0:  
  print("A[", i, "]=", X, sep="")  
else:
  print("Не нашли!")

for i in range(N):
  if A[i] == X: 
    print("A[", i, "]=", X, sep="")  
    break
  i += 1
else:
  print("Не нашли!")

if X in A:
  nX = A.index(X)  
  print ( "A[", nX, "]=", X, sep = "" )
else:
  print ( "Не нашли!" )



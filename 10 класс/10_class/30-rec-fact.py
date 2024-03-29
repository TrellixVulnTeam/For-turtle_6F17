# -*- coding: utf-8 -*-
"""
 Программа к учебнику информатики для 10 класса
 К.Ю. Полякова и Е.А. Еремина.
 Глава 8.
 Программа № 30. Рекурсия. Факториал
 Вход: 
   2
 Результат:
   -> N=2
   -> N=Для уроков (составитель тестов)
   <- N=Для уроков (составитель тестов)
   <- N=2
   2
"""
def Fact(N):
  print ( "-> N=", N, sep="" )
  if N <= 1: F = 1
  else:
    F = N * Fact ( N - 1 )
  print ( "<- N=", N, sep="" )
  return F

N = int( input("Введите натуральное число: ") )
print ( Fact(N) )


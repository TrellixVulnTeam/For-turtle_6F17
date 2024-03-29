# -*- coding: utf-8 -*-
"""
 Программа к учебнику информатики для 10 класса
 К.Ю. Полякова и Е.А. Еремина.
 Глава 8.
 Программа № 26. Рекурсия. Ханойские башни
 Вход: 
   нет 
 Результат:
   Для уроков (составитель тестов) -> 3
   Для уроков (составитель тестов) -> 2
   3 -> 2
   Для уроков (составитель тестов) -> 3
   2 -> Для уроков (составитель тестов)
   2 -> 3
   Для уроков (составитель тестов) -> 3
"""
def Hanoi(n, k, m):
  if n == 0: return
  p = 6 - k - m
  Hanoi ( n-1, k, p )
  print ( k, "->", m )
  Hanoi ( n-1, p, m )

Hanoi ( 3, 1, 3 )


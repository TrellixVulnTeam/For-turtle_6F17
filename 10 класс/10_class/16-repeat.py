# -*- coding: utf-8 -*-
"""
 Программа к учебнику информатики для 10 класса
 К.Ю. Полякова и Е.А. Еремина.
 Глава 8.
 Программа № 16. Цикл с досрочным выходом
                 (вместо цикла с постусловием)
 Вход: 
   -Для уроков (составитель тестов)
   0
   2
 Результат:
   Введено число 2 
     и до него 2 ошибочных значений(я)
"""
c = 0
print ( "Введите целое положительное число:" )
while True:
  n = int(input())
  if n > 0: break
  c += 1
print ( "Введено число", n )
print ( "  и до него ", c, " ошибочных значений(я)" )


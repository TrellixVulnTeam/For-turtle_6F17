# -*- coding: utf-8 -*-
"""
 Программа к учебнику информатики для 10 класса
 К.Ю. Полякова и Е.А. Еремина.
 Глава 8.
 Программа № 20. Программа с процедурой
 Вход: 
   -Для уроков (составитель тестов)
 Результат:
   Ошибка программы
"""
def Error():
  print ( "Ошибка программы" )

n = int( input() )
if n < 0:
  Error()


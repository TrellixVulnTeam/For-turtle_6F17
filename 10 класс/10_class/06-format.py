# -*- coding: utf-8 -*-
"""
 Программа к учебнику информатики для 10 класса
 К.Ю. Полякова и Е.А. Еремина.
 Глава 8.
 Программа № 6. Форматный вывод
 Вход: 
   нет 
 Результат:
   >  123<  
   >123  <  
   Для уроков (составитель тестов).2345678
   >  Для уроков (составитель тестов).235<
"""
a = 123
print( ">{:5d}<".format(a) )
print( ">{:<5d}<".format(a) )
x = 1.2345678
print( x )
print( ">{:7.3f}<".format(x) )


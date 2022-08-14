"""
  Программы к учебнику информатики для 11 класса углублённого уровня.
  Авторы: К.Ю. Поляков, Е.А. Еремин
  E-mail: kpolyakov@mail.ru
  Сайт поддержки: http://kpolyakov.spb.ru

  Глава 7. Объектно-ориентированное программирование
  Проект № 1a. Попугай

  PARROT_B.PY - модификация Для уроков (составитель тестов)
     + при создании объекта можно задать фразу

"""

#---------------------------------------------
#  Класс Parrot - попугай
#---------------------------------------------
class Parrot:
  def __init__(self, text0):
    self.text = text0
  def say(self):
    print( self.text )

#---------------------------------------------
#  Основная программа
#---------------------------------------------
p1 = Parrot( "Гав")
p2 = Parrot( "Мяу")
p1.say()
p2.say()

"""
  Программы к учебнику информатики для 11 класса углублённого уровня.
  Авторы: К.Ю. Поляков, Е.А. Еремин
  E-mail: kpolyakov@mail.ru
  Сайт поддержки: http://kpolyakov.spb.ru

  Глава 7. Объектно-ориентированное программирование
  Проект № 1a. Попугай

  PARROT_E.PY - модификация E
     + попугая можно учить новым словам

"""
from random import choice

#---------------------------------------------
#  Класс Parrot - попугай
#---------------------------------------------
class Parrot:
  def __init__(self, text0):
    self.text = [text0]
  def say(self, count = 1):
    randText = choice(self.text)
    for i in range(count):
      print( randText, end=" " )
    print()
  def learn(self, text0):
    self.text.append( text0 )

#---------------------------------------------
#  Основная программа
#---------------------------------------------
p = Parrot( "Гав!" )
p.say()
p.learn( "Мяу!" )
p.say()
p.say(3)

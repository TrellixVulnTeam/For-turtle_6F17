"""
  Программы к учебнику информатики для 11 класса углублённого уровня.
  Авторы: К.Ю. Поляков, Е.А. Еремин
  E-mail: kpolyakov@mail.ru
  Сайт поддержки: http://kpolyakov.spb.ru

  Глава 7. Объектно-ориентированное программирование
  Проект № 1b. Ряд лампочек - управление состоянием

  LAMPROW_B.PY - модификация Для уроков (составитель тестов)
     + количество лампочек в цепочке задаётся в конструкторе

"""

#---------------------------------------------
#  Класс LampRow - ряд лампочек
#---------------------------------------------
class LampRow:
  def __init__( self, count0 = 8 ):
    self.count = count0
    self.__state = '0'*count0
  def __getState( self ):
    return self.__state
  def __setState( self, newState ):
    if len(newState) != self.count:
      newState = '00000000'
    self.__state = newState
  state = property (__getState, __setState)
  def show( self ):
    for c in self.__state:
      if c == '0':
        print("-", end='')
      else:
        print("*", end='')
    print()

#---------------------------------------------
#  Основная программа
#---------------------------------------------
lamps = LampRow( 6 )
lamps.show()
lamps.state = "101010"
print( lamps.state )
lamps.show()
lamps.state = "10101010"
print( lamps.state )
lamps.show()
"""
  Программы к учебнику информатики для 11 класса углублённого уровня.
  Авторы: К.Ю. Поляков, Е.А. Еремин
  E-mail: kpolyakov@mail.ru
  Сайт поддержки: http://kpolyakov.spb.ru

  Глава 7. Объектно-ориентированное программирование
  Проект № 1b. Ряд лампочек - управление состоянием

  LAMPROW_A.PY - начальный вариант

"""

#---------------------------------------------
#  Класс LampRow - ряд лампочек
#---------------------------------------------
class LampRow:
  def __init__( self ):
    self.count = 8
    self.__state = '00000000'
  def __getState( self ):
    return self.__state
  def __setState( self, newState ):
    if len(newState) != 8:
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
lamps = LampRow()
lamps.show()
lamps.state = '10101010'
print( lamps.state )
lamps.show()
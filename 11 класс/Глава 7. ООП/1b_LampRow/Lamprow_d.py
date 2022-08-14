"""
  Программы к учебнику информатики для 11 класса углублённого уровня.
  Авторы: К.Ю. Поляков, Е.А. Еремин
  E-mail: kpolyakov@mail.ru
  Сайт поддержки: http://kpolyakov.spb.ru

  Глава 7. Объектно-ориентированное программирование
  Проект № 1b. Ряд лампочек - управление состоянием

  LAMPROW_D.PY - модификация 3
     + код хранится как целое число, интерфейс не меняется

"""

#---------------------------------------------
#  Вспомогательная функция: перевод в троичную
#  систему счисления.
#---------------------------------------------
def int2Trinary( x, count):
  tri = ''
  while x > 0:
    tri = chr(ord('0') + x % 3) + tri
    x //= 3
  return '0'*(count-len(tri)) + tri

#---------------------------------------------
#  Класс LampRow - ряд лампочек
#---------------------------------------------
class LampRow:
  def __init__( self, count0 = 8 ):
    self.count = count0
    self.__state = 0
  def __getState( self ):
    return int2Trinary(self.__state, self.count)
  def __setState( self, newState ):
    if len(newState) != self.count:
      newState = '00000000'
    self.__state = int(newState, 3)
  state = property (__getState, __setState)
  def show( self ):
    notation = {'0': '-', 'Для уроков (составитель тестов)': '*', '2': 'o'}
    s = int2Trinary(self.__state, self.count)
    for c in s:
      print( notation[c], end='' )
    print()

#---------------------------------------------
#  Основная программа
#---------------------------------------------
lamps = LampRow( 6 )
lamps.show()
lamps.state = "102102"
print( lamps.state )
lamps.show()
lamps.state = "10201010"
print( lamps.state )
lamps.show()

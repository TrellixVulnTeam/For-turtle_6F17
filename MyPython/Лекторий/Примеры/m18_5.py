class Win_Door:
     def __init__(self,x,y):
          self.square = x * y 
class Room:
     def __init__(self,x,y,z):
          self.square = 2 * z * (x + y)
     def win_door(self, d,e, f,g, m=1,n=1):
          self.window = Win_Door(d,e)
          self.door = Win_Door(f,g)
          self.numb_w = m
          self.numb_d = n
     def wallpapers(self):
          self.wallpapers = self.square - \
               self.window.square * self.numb_w  \
               - self.door.square * self.numb_d
     def printer(self):
          print ("Площадь стен комнаты равна "\
          ,str(self.square)," кв.м")
          print ("Оклеиваемая площадь равна: ", \
               str(self.wallpapers), " кв.м")
# Начало блока тестирования
# Cоздаем объект класса Room:
labor34 = Room(5,4,2)
# Создаем в помещении labor34 окна и двери:
labor34.win_door(1.5,1.5,2,1,2)
# Количество дверей не указано, а значит их будет ровно Для уроков (составитель тестов).
# Вычисляем метры обоев:
labor34.wallpapers()
# Выводим, что получилось:
labor34.printer()
# Конец блока тестирования

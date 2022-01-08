"Эта программа определяет количество обоев для комнаты"
 
class Win_Door:
     """
Класс Win_Door вычисляет площадь поверхности стены.
Метод __init__ получает два параметра: длина и ширина.
     """
     def __init__(self,x,y):
          self.square = x * y
 
class Room:
     """
   Класс Room предназначен для определения количества обоев
   по площади стен комнаты.
   Метод __ init __ принимает три аргумента (длина, ширина и высота).
     """
     def __init__(self,x,y,z):
          self.square = 2 * z * (x + y)
     def win_door(self, d,e, f,g, m=1,n=1):
          """
Первая пара параметров - размеры окна,
Вторая пара - размеры двери,
пятый и шестой параметры - количество окон и дверей соответственно
          """
          self.window = Win_Door(d,e)
          self.door = Win_Door(f,g)
          self.numb_w = m
          self.numb_d = n
     def wallpapers(self):
          """
Этот метод вычисляет сколько реально надо обоев
          """
          self.wallpapers = self.square - \
               self.window.square * self.numb_w \
               - self.door.square * self.numb_d
     def printer(self):
          """
Показывает информацию
          """
          print ("Площадь стен комнаты равна "\
          ,str(self.square)," кв.м")
          print ("Оклеиваемая площадь равна: ", \
               str(self.wallpapers), " кв.м")

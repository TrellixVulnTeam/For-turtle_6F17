class YesInit:
     def __init__(self,one,two):    # Конструктор класса
          self.fname = one
          self.sname = two

class NoInit:                       # Класс без конструктора
     def names(self,one,two):
          self.fname = one
          self.sname = two

# Создаем объект и задаем значения атрибутом 
obj1 = YesInit("Все хорошо,","прекрасная маркиза")
 
print (obj1.fname, obj1.sname)      # Выводим значения fname и sname
 
obj2 = NoInit()                     # Создаем объект

# Задаем значения атрибутов с помощью метода
obj2.names("Все хорошо,","прекрасная маркиза")
print (obj2.fname, obj2.sname)      # Выводим значения fname и sname

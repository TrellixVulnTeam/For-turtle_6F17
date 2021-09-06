class Things:
     def __init__(self,n,t):
          self.имя = n
          self.итог = t
 
th1 = Things("Стол", 5)
th2 = Things("Компьютер", 7)
 
print (th1.имя,th1.итог) # Вывод: table 5
print (th2.имя,th2.итог) # Вывод: computer 7
 
th1.цвет = "Зеленый" # новое свойство объекта th1
 
print (th1.цвет) # Вывод: green
print (th2.цвет) # ОШИБКА: у объекта th2 нет свойства цвет!

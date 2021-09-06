class Second:
     цвет  = "red"                      # цвет по умолчанию
     форма = "circle"                   # форма по умолчанию
     def changecolor(self,newcolor):    # параметр может менять цвет
          self.цвет = newcolor
     def changeform(self,newform):      # параметр может менять форму
          self.форма = newform
# Здесь в классе с помощью атрибутов вне функции устанавливаются
# два свойства объектов: красный цвет и круглая форма. А методы могут
# менять эти свойства в зависимости от пожеланий тех, кто создает объекты. 
obj1 = Second()
obj2 = Second()
 
print (obj1.цвет, obj1.форма)   # вывод на экран "red circle"
print (obj2.цвет, obj2.форма)   # вывод на экран "red circle"
 
obj1.changecolor("green")       # изменение цвета первого объекта
obj2.changecolor("blue")        # изменение цвет второго объекта
obj1.changeform("rectangle")    # изменение формы первого объекта
obj2.changeform("oval")         # изменение формы второго объекта
 
print (obj1.цвет, obj1.форма)   # вывод на экран "green rectangle"
print (obj2.цвет, obj2.форма)   # вывод на экран "blue oval"

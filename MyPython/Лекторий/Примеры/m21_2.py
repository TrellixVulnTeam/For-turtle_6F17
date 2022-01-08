class Basket:
#создаём класс Basket ("корзина")
     def __init__ (self, contents=[]) :
         self.contents = contents[:]
				
     def __add__ (self, element):
         return Basket(self.contents + element)
		
     def __str__ (self):
         result = ""
         for element in self.contents:
             result = result + " " + element
         return "Старая дырявая корзина содержит:" + result
        
b = Basket (['яблоко', 'апельсин'])
b +=['лимон']
print(b)


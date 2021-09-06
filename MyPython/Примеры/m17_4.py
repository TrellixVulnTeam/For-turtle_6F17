class Стол:
     def __init__(self,l,w,h):
          self.длина = l
          self.ширина = w
          self.высота = h
     def outing(self):
          print (self.длина,self.ширина,self.высота)
 
class Кухня(Стол):
     def howplaces(self,n):
          if n < 2:
               print ("В этой кухне нет стола")
          else:
               self.places = n
     def outplases(self):
          print (self.places)
 
t_room1 = Кухня(2,1,0.5)
t_room1.outing()
t_room1.howplaces(5)
t_room1.outplases()
 
t_2 = Стол(1,3,0.7)
t_2.outing()
t_2.howplaces(8) # ОШИБКА

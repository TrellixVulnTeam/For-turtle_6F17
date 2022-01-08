class One:
     def __init__(self,a):
          self.a = a ** 2
 
class Two:
     def __init__(self,a):
          self.a = a * 2
 
a = input ("введите число ")
a = int(a)
if -100 < a < 100:
     obj = One(a)
else:
     obj = Two(a)
 
print (obj.a) 

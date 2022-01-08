class Newclass:
     def __init__(self, base):
          self.base = base
     def __add__(self, a):
          self.base = self.base + a
     def __str__(self):
          return "%s !!! " % self.base
 
a = Newclass(10)
a + 20
print (a)
 
b = Newclass("yes")
b + "terday"
print (b)
 
c = Newclass([2,6,3])
c + [7, 1]
print (c)

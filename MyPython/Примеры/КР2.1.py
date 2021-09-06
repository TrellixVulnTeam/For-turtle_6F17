from math import sqrt
x=int(input("Введите координату точк Х "))
y=int(input("Введите координату точк Y "))
r=int(input("Введите радиус круга "))
if sqrt(x*x+y*y)>=r:
    print("Точка не принадлежит кругу")
else:
    print("Точка принадлежит кругу")

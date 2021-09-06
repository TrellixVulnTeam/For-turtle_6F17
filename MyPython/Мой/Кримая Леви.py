from turtle import *

speed(0)
penup()
goto(-300, -300)
l = 300
ht()


pendown()
right(45)

def Levi(l, n = 0):
    if n == 0:
        forward(l)
    else:
        left(90)
        Levi(l / 2 ** (1 /  2), n-1)

    right(90)

    if n == 0:
        forward(l)
    else:
        left(90)
        Levi(l / 2 ** (1 /  2), n-1)

    
Levi(l, 10)

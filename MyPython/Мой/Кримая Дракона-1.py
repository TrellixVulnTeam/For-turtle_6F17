from turtle import *

speed(1)
penup()
#goto(-300, -300)
l = 200
ht()
right(90)
pendown()

def Drako(l, n = 0):

    if n == 0:
        forward(l)
        right(90)
        forward(l)
    else:
        left(45)
        Drako(l / 2 ** (1 / 2), n - 1)

    if n == 0: right(90)        

    if n == 0:
        forward(l)
        left(90)
        forward(l)        
    else:
        right(90)
        Drako(l / 2 ** (1 / 2), n - 1)        

Drako(l, 1)


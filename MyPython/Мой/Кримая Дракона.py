from turtle import *

speed(0)
penup()
#goto(-300, -300)
l = 10
ht()

pendown()

def Drako(l, n = 0):
    forward(l)

    a(l, n - 1)

def a(l, n):
    if n == 0:
        return
    print(n)
    a(l, n - 1)
    right(90)
    b(l, n - 1)
    forward(l)
    right(90)

def b(l, n):
    if n == 0:
        return
    print(n)
    left(90)
    forward(l)
    a(l, n - 1)
    left(90)
    b(l, n - 1)
        
    


Drako(l, 10)


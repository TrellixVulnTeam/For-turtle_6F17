from turtle import *

a = int(input("Сторона квадрата "))
n = int(input("число поворотов "))

speed(0)
penup()
goto(-400,-350)
pendown()
left(90)

def kv(a=300):
    for i in range(4):
        forward(a)
        right(90)

def zig(a, x, n, q):

    for i in range(n):
        right(90 * q)
        a -= (2 * x) * q
        forward(a)    
    return a

def kr(a, n=1):
    x = a / (n * 2)   
    forward(a - x)
    a = zig(a, x, n, 1)
    forward(x * 2)
    zig(a, x, n - 1, -1)       
   
kv(a)

kr(a, n)
penup()
home()
goto(-400, -350 + a)
pendown()
kr(a, n)

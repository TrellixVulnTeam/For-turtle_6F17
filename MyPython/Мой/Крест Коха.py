from turtle import *

hideturtle()
speed(0)
penup()
left (135)

x = 0
y = -300
size = 400

setposition(x,y)

pendown()


    
def s(size, n=0):
    if n == 0:
        forward (size)
    else:
        s(size / 3, n - 1)
        left (-90)
        s(size / 3, n - 1)
        right (-90)
        s(size / 3, n - 1)
        right (-90)
        s(size / 3, n - 1)
        left(-90)
        s(size / 3, n - 1)

def koh (size, n):
    for i in range(4):
        s (size, n)
        right (360/4)

q = int(input("Число вложений "))
koh (size, q)

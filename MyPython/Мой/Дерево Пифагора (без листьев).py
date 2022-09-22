from turtle import *

hideturtle()
speed(0)
penup()
left (90)

x = 0
y = -300
size = 150

setposition(x,y)

pendown()


def kv (size, n=0):
    forward (size)
    if n != 0:
        left (45)
        kv(size / 2 ** (1 / 2), n-1)
        right(90)
        kv(size / 2 ** (1 / 2), n-1)
        left (45)
    backward(size)


kv(size, 10)

done()

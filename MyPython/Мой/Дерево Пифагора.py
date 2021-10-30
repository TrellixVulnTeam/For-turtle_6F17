from turtle import *

hideturtle()
speed(0)
penup()
left (90)

x = 0
y = -400
size = 150

setposition(x,y)



def k (size):
    penup()
    left (45)
    aux = size * (2 ** (1/2))/2
    forward (aux)
    right (135)
    pendown()

    for i in range (4):
        forward (size)
        right (90)

    penup()
    right (45)
    forward(aux)
    left (135)
    

def kv (size, n=0):
    forward (size)
    k(size)
    forward (size/2)
    if n != 0:
        left (45)
        kv(size / 2 ** (1 / 2), n-1)
        right(90)
        kv(size / 2 ** (1 / 2), n-1)
        left (45)
    backward(size * 1.5)

n = int(input("Число уровней дерева Пифагора "))
kv(size, n)

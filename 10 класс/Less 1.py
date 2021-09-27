from turtle import *

def квадрат(сторона = 40):
    pendown()
    speed(0)
    for i in range(4):
        forward(сторона)
        left(90)
    penup()

сторона = int(input("Введи величину стороны "))
for i in range(8):
    квадрат(сторона)
    left(45)

from turtle import *

size=50
n = 10
x = 80
angle = -90 + x
left(45 - x/2)


for i in range(n*2):
    forward(size)
    left(angle*(-1)**i)


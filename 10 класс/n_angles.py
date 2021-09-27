from turtle import *

def n_angles(n=3, side=100):
    for i in range(n):
        forward(side)
        left(360/n)

left(90)
for i in range(3, 11):
    n_angles(i)
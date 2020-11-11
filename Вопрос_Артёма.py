from turtle import *
fw = forward
bw = backward
l = left
r = right
size = 30


def линия(s):
    pendown()
    for i in range(12):
        fw(s)
        stamp()
        bw(s)
        l(30)


линия(size)
линия(size + 20)

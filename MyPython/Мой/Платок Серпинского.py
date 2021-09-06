from turtle import*
from random import*

def point (p, d, c):
    d = [(d[0]+p[0])/2, (d[1]+p[1])/2]
    goto (d)
    dot(5, c)    
    return d

def begining (k = 350):
    penup()
    hideturtle()
    speed(0)

    t = [[-k, -k], [k, -k] ,[0, k]]

    for x in t:
        goto (x)
        dot(5)

    fractal (k, t)

def fractal(k, t):
    d = [randrange(-k,k), randrange(-k,k)]
    goto (d)
    dot(5)
    for i in range (10000):
        rand = randrange(1,4)
        if rand == 1:
            d = point (t[0], d, "blue")
        elif rand == 2:
            d = point (t[1], d, "red")
        elif rand == 3:
            d = point (t[2], d, "green")

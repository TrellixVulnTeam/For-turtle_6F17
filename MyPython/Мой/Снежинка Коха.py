from turtle import *

speed(0)
division = 2.5
penup()
left (90)
size = 400
setposition(-300,-400)
pendown()
    
def s(size, n=0):
    if n == 0:
        forward (size)
    else:
        for j in (60,-120,60):
            s(size / division, n - 1)
            left (j)
        s(size / division, n - 1)

def koh (size, n):
    for i in range(3):
        s (size, n)
        right (120)

q = int(input("Число вложений "))
koh (size, q)
done()

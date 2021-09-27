import turtle as t


def sierpinski(n,size):
    if n==0:
        t.begin_fill()
        for i in range(3):
            t.forward(size)
            t.left(120)
        t.end_fill()

    else:
       sierpinski(n - 1, size / 2)
       t.forward(size/2)
       sierpinski(n - 1, size / 2)
       t.forward(size/2)
       t.left(120)
       t.forward(size/2)
       sierpinski(n - 1, size / 2)
       t.forward(size/2)
       t.left(120)
       t.forward(size)
       t.left(120)


t.speed(0)
t.hideturtle()
sierpinski(6, 600)
t.done()

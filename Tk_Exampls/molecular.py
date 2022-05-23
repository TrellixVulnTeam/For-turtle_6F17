from tkinter import *


def motion():
    global xi
    global yi
    global v

    if (x - r) <= c.coords(ball)[0] + v < (x - r) + v:
        xi = -v + 0.3
        c.itemconfig(ball, fill='yellow')
    if -v < c.coords(ball)[0] - v <= 0:
        xi = v - 0.3
        c.itemconfig(ball, fill='blue')
    if (y - r) <= c.coords(ball)[1] + v < (y - r) + v:
        yi = -v
        c.itemconfig(ball, fill='red')
    if -v < c.coords(ball)[1] - v <= 0:
        yi = v
        c.itemconfig(ball, fill='green')

    c.move(ball, xi, yi)
    window.after(10, motion)


x = 800
y = 300
r = 50
v = 5

xi = v
yi = v

window = Tk()
c = Canvas(width=x, height=y, bg='white')
c.pack()
ball = c.create_oval(60, 40, 60 + r, 40 + r, fill='green')

motion()

window.mainloop()

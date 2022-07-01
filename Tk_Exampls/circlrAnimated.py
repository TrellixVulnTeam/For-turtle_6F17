import tkinter


def moves():
     = X
    X += V
    if X > x:
        X = 0
    canvas.move(o, X - oldX, 0)
    canvas.update()


x = 500
y = 200

V = 5


window = tkinter.Tk()
window.title('Дорога и машины')
window.geometry(str(x) + 'x' + str(y))

canvas = tkinter.Canvas(window, bg="white", width=x, height=y)
canvas.align = "client"
canvas.pack()
o = canvas.create_oval(10,10,40,40)
c.

window.mainloop()

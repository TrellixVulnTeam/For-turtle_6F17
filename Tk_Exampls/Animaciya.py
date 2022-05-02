import tkinter


class TRoad:
    def __init__(self, length0, width0):
        if length0 > 0:
            self.length = length0
        else:
            self.length = 0
        if width0 > 0:
            self.width = width0
        else:
            self.width = 0


class TCar:
    def __init__(self, road0, p0, v0, imgName, canvas):
        self.road = road0
        self.P = p0
        self.V = v0
        self.X = 0
        self.pic = tkinter.PhotoImage(file=imgName)
        self.img = None
        self.canvas = canvas

    def move(self):
        oldX = self.X
        self.X += self.V
        if self.X > self.road.length:
            self.X = 0
        self.canvas.move(self.img, self.X - oldX, 0)
        self.canvas.update()

    def show(self):
        if not self.img:
            self.img = self.canvas.create_image(self.X, 55 * self.P, anchor='nw', image=self.pic)


def animate():
    for i in range(N):
        cars[i].move()
    canvas.after(25, animate)  # повторный вызов через 25 мс


x = 500
y = 200

window = tkinter.Tk()
window.title('Дорога и машины')
window.geometry(str(x) + 'x' + str(y))

canvas = tkinter.Canvas(window, bg="white", width=x, height=y)
canvas.align = "client"
canvas.pack()

road = TRoad(x - 60, 3)

N = 3
cars = []
for i in range(N):
    car = TCar(road, i + 1, 2 * (i + 1), "car" + str(i + 1) + ".gif", canvas)
    cars.append(car)
    car.show()

canvas.after(0, animate)
canvas.mainloop()

print("Дорога: длина = ", road.length, "; ширина = ", road.width, sep="")
print("Свойства машин:")
for i in range(N):
    print(i, ": P = ", cars[i].P, "; V = ", cars[i].V, "; X = ", cars[i].X, sep="")

print("Координаты машин:")
for i in range(N):
    print("X[", i, "] = ", cars[i].X, sep="")

window.mainloop()

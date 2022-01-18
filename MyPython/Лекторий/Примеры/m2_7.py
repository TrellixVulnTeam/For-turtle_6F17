from tkinter import *
from time import *

window = Tk()                 # Вывод окна
window.title(" Начало ")      # заголовок окна
window.geometry('500x500')    # размер окна

canv = Canvas(window, bg='white', width=500, height=500) # задать холст для рисования
canv.pack() # вывести холст

# произвольный многоугольник: сколько пар координат добавите, столько вершин и будет

canv.create_polygon(30, 30, 100, 30, 80, 60, 50, 60, fill='red', outline="black", smooth=0)
x=100
y=100
X0=[x,y]
X1=[x+50,y-10]
X2=[x+75,y+10]
X3=[x+50,y+60]
X4=[x,y+70]
X5=[x-20,y+55]
X6=[x,y+35]
X7=[x+40,y+10]
canv.create_polygon(X0, X1, X2, X3, X4, X5, X6, X7, fill='gold', outline="black", smooth=1)

canv.mainloop()
from tkinter import *
from time import *

окно = Tk()                 # Вывод окна
окно.title(" Начало ")      # заголовок окна
окно.geometry('500x500')    # размер окна

холст = Canvas(окно, bg='white', width=500, height=500) # задать холст для рисования
холст.pack() # вывести холст

# произвольный многоугольник: сколько пар координат добавите, столько вершин и будет

холст.create_polygon(30,30,100,30,80,60,50,60,fill='red',outline="black",smooth=0)
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
холст.create_polygon(X0,X1,X2,X3,X4,X5,X6,X7, fill='gold',outline="black",smooth=1)

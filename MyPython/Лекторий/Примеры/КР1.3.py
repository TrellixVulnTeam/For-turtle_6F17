from tkinter import *
from time import *

окно = Tk()                 # Вывод окна
окно.title(" Начало ")      # заголовок окна
окно.geometry('800x800')    # размер окна
холст = Canvas(окно, bg='#FFFFFF', width=800, height=800) # задать холст для рисования
холст.pack() # вывести холст
радиус=float(input("Введите радиус внешней окружности"))
t1=(400-радиус,400-радиус)
t2=(400+радиус,400+радиус)
холст.create_oval(t1,t2, width=0, fill="red")
t1=(400-радиус/2,400-радиус/2)
t2=(400+радиус/2,400+радиус/2)
холст.create_oval(t1,t2, width=0, fill="#FFFFFF")

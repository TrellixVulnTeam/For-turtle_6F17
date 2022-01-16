from tkinter import *
from time import *

окно = Tk()                 # Вывод окна
окно.title(" Начало ")      # заголовок окна
окно.geometry('400x250')    # размер окна

холст = Canvas(окно, bg='white', width=480, height=240) # задать холст для рисования
холст.pack() # вывести холст

холст.create_rectangle(100,20,300,240,fill="lightgreen") # прямоугольник
холст.create_rectangle(120,40,280,220,outline="gray",width=6,fill="lightblue")

холст.mainloop()
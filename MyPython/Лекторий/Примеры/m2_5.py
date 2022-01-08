from tkinter import *
from time import *

окно = Tk()                 # Вывод окна
окно.title(" Начало ")      # заголовок окна
окно.geometry('500x250')    # размер окна

холст = Canvas(окно, bg='white', width=480, height=240) # задать холст для рисования
холст.pack() # вывести холст

холст.create_oval(30,10,170,80, outline="red",width=5, fill="chocolate") # нарисовать на холсте овал
холст.create_oval(30,100,170,240,fill="green") # нарисовать на холсте овал
холст.create_oval(250,100,400,170,width=5,fill="yellow") # нарисовать на холсте овал

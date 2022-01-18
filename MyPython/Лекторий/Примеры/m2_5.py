from tkinter import *
from time import *

window = Tk()                 # Вывод окна
window.title(" Начало ")      # заголовок окна
window.geometry('500x250')    # размер окна

canv = Canvas(window, bg='white', width=480, height=240) # задать холст для рисования
canv.pack() # вывести холст

canv.create_oval(30, 10, 170, 80, outline="red", width=5, fill="chocolate") # нарисовать на холсте овал
canv.create_oval(30, 100, 170, 240, fill="green") # нарисовать на холсте овал
canv.create_oval(250, 100, 400, 170, width=5, fill="yellow") # нарисовать на холсте овал

canv.mainloop()
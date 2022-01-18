from tkinter import *
from time import *

window = Tk()                 # Вывод окна
window.title(" Начало ")      # заголовок окна
window.geometry('500x500')    # размер окна

canv = Canvas(window, bg='white', width=500, height=500) # задать холст для рисования
canv.pack() # вывести холст

canv.create_oval(30, 10, 130, 110, fill="orange") # нарисовали на холсте овал
canv.create_rectangle(180, 60, 280, 160, tag="rect", fill="lightgreen")
canv.create_text(220, 20, fill="VioletRed", font="arial", text="Вот попробуйте...")

canv.mainloop()
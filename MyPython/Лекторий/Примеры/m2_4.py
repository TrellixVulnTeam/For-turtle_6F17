from tkinter import *
from time import *

window = Tk()                 # Вывод окна
window.title(" Начало ")      # заголовок окна
window.geometry('800x600')    # размер окна

canv = Canvas(window, bg='white', width=800, height=600) # задать холст для рисования
canv.pack() # вывести холст

# линия
canv.create_line(0,300, 800, 300, width=10, fill='blue')

canv.mainloop()
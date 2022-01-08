from tkinter import *
from time import *

окно = Tk()                 # Вывод окна
окно.title(" Начало ")      # заголовок окна
окно.geometry('800x600')    # размер окна

холст = Canvas(окно, bg='white', width=800, height=600) # задать холст для рисования
холст.pack() # вывести холст

# линия
холст.create_line(0,300, 800, 300, width=10, fill='blue') 


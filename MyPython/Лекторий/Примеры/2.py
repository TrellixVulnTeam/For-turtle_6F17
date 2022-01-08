from tkinter import *
from time import *

окно = Tk()                 # Вывод окна
окно.title(" Начало ")      # заголовок окна
окно.geometry('800x800')    # размер окна

холст = Canvas(окно, bg='white', width=800, height=800) # задать холст для рисования
холст.pack() # вывести холст
def kvadrat(a,b):
    холст.create_rectangle(a,a,a+100,a+100, width=2, fill=b) # нарисовать на холсте овал

for a in range(0,700,50):
    kvadrat(a,"red")
    
    

from tkinter import *
from random import *

окно = Tk()                 # Вывод окна
окно.title(" ММденс ")      # заголовок окна
окно.geometry('500x250')    # размер окна

холст = Canvas(окно, bg='white', width=480, height=240) # задать холст для рисования
холст.pack() # вывести холст

col = ["lavender", "SlateBlue","green","yellow","chocolate","DeepPink","BlueViolet",
       "purple2","red1","coral1","wheat1","gold1","SpringGreen1","orange"]

for i in range(500):
    x = randint(-20,480); y = randint(-20,240)
    a = randint(10,60); b = randint(10,60)
    с = randint(0,13)
    холст.create_oval(x,y,x+a,y+b,fill=col[с]) # нарисовали на холсте овал

from tkinter import *
from random import *

def clrandom():
    a = lambda: randint(0,255)
    x=a()
    color='#%02X%02X%02X' % (x,x,x)
    return color

#Как использовать: например, fill=clrandom()
окно = Tk()                 # Вывод окна
окно.title(" Начало ")      # заголовок окна
окно.geometry('800x800')    # размер окна

холст = Canvas(окно, bg='white', width=800, height=800) # задать холст для рисования
холст.pack() # вывести холст
def kvadrat(x,y,z):
    холст.create_rectangle(x*0.4,x,x*0.4+80,x+80, outline=z, width=randint(2, 10), fill=y) # нарисовать на холсте овал

def krug(x,y,z):
    s=200
    r=50
    холст.create_oval(x+s,x,(x+s)*1.1+r,(x)*1.1+r, outline=z, width=randint(2, 10), fill=y) # нарисовать на холсте овал

for a in range(10, 500, 30):
    kvadrat(a,clrandom(),clrandom())
    krug(a,clrandom(),clrandom())
    
    

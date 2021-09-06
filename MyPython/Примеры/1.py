#изменение имён функций
печать = print
ввод = input
целое = int
дробное = float
#программа
#высота = дробное(ввод("Ввкдите высоту параллелепипеда "))
#ширина = дробное(ввод("Ввкдите ширину параллелепипеда "))
#глубина = дробное(ввод("Ввкдите глубину параллелепипеда "))
#объём = глубина*ширина*высота
#площадь = 4*(глубина*высота)+2*(глубина*ширина)
#печать("Объём ", объём, "\nПлощадь поверхности", площадь)
#графика
from tkinter import *
окно = Tk()
окно.title("Параллелограм")
окно.geometry('500x500')
холст=Canvas(окно, bg='LightSteelBlue', width=490, height=490)
холст.pack()

x1=y1=0
a=int(input("Какой размер флага нужен "))
#Россия
холст.create_rectangle(x1,y1,x1+a,y1+a/3, width=0 ,fill="#FFFFFF")
холст.create_rectangle(x1,y1+a/3,x1+a,y1+2*a/3, width=0 ,fill="#0000FF")
холст.create_rectangle(x1,y1+a/3*2,x1+a,y1+a, width=0 ,fill="#FF0000")
#Германия
x1=y1=x1+a
холст.create_rectangle(x1,y1,x1+a,y1+a/3, width=0 ,fill="#000000")
холст.create_rectangle(x1,y1+a/3,x1+a,y1+2*a/3, width=0 ,fill="#FF0000")
холст.create_rectangle(x1,y1+a/3*2,x1+a,y1+a, width=0 ,fill="gold")
#Франция
x1=y1=x1+a
холст.create_rectangle(x1,y1,x1+a/3,y1+a, width=0 ,fill="#0000ff")
холст.create_rectangle(x1+a/3,y1,x1+2*a/3,y1+a, width=0 ,fill="#FFFFFF")
холст.create_rectangle(x1+a/3*2,y1,x1+a,y1+a, width=0 ,fill="#FF0000")

#Линии
холст.create_line(0,0,500,500, width=10 ,fill="#FFFF00")
холст.create_line(0,500,500,0, width=10 ,fill="#0000FF")
холст.create_line(250,0,250,500, width=10 ,fill="#00FF00")

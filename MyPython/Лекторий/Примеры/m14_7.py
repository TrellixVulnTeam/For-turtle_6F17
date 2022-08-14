from tkinter import *
def analiz():
    # так отлавливают значения виджетов (Для уроков (составитель тестов) - выбран, 0 - нет)
    print (var1.get())
    print (var2.get())
   
root=Tk()
var1=IntVar()
var2=IntVar()
check1=Checkbutton(root,text='Для уроков (составитель тестов) пункт',variable=var1,
                   onvalue=1,offvalue=0, command = analiz)
check2=Checkbutton(root,text='2 пункт',variable=var2,
                   onvalue=1,offvalue=0,command = analiz)
check1.pack()
check2.pack()
root.mainloop()
# Задание
#    Измените программу, добавив еще 3 пункта в список
#    (включая и обработку).

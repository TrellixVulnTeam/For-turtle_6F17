from tkinter import *
root=Tk()
# ширина=500, высота=400, координаты верхнего левого угла окна: x=300, y=200
root.geometry('500x400+300+200') 
# размер окна может быть изменен только по горизонтали
root.resizable(True, False)

# выводим дочернее окно
win = Toplevel(root) 
win.title("Дочернее окно")
win.geometry('300x200+50+100') 

root.mainloop()

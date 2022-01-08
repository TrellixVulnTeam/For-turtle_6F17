from tkinter import *
root = Tk()
def getV(root):
    a = scale1.get()
    print ("Значение", a)
    
scale1 = Scale(root,orient=HORIZONTAL,length=300,from_=50,
               to=80,tickinterval=5,resolution=5,command = getV)
scale1.pack()
root.mainloop()
# Задание
#   Измените программу так, чтобы шкала была вертикальной, 
#   градация была от 0 до 100 с шагом 10.
#   Данная шкала должна показывать, например, радиус круга.
#   При изменении шкалы должен соответственно менять и нарисованный
#   круг.

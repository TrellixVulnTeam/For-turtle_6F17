from tkinter import *
def find():
    print(var.get())
    
root=Tk()
var=IntVar()
rbutton1=Radiobutton(root,text='Раз',
                     variable=var,value=1, command = find)
rbutton2=Radiobutton(root,text='Два',
                     variable=var,value=2, command = find)
rbutton3=Radiobutton(root,text='Три',
                     variable=var,value=3, command = find)
rbutton1.pack()
rbutton2.pack()
rbutton3.pack()
root.mainloop()
# Задание
# Добавьте еще один виджет Radiobutton.
# Измените программ так, чтобы в окне рисовались: при выборе
# виджета Раз - квадрат, Два - овал (предыдущий должен уничтожаться),
# Три - ромб (предыдущий удалялся), Четыре - Слово "МАЙ" (предыдущий удалялся)

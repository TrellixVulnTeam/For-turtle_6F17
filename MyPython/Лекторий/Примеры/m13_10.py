from tkinter import *
root = Tk()
root.title('Пример использования Entry')
root.geometry(newGeometry="300x200+500+250")

# выведем окно на 20 символов
ent1 = Entry(root,width=20,bd=3)

ent1.pack(side ='top' )
button = Button(root,text='OK',width=9)
button.pack(side = 'top')
root.mainloop()

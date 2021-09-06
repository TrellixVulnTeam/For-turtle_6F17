from tkinter import *
root=Tk()  # создали окно
# создали кнопку и задали ее свойство
button1=Button(root,text='ok',width=25,
               height=5,bg='black',
               fg='red',font='arial 24')
button1.pack() # вывели кнопку с помощью упаковщика pack
root.mainloop()

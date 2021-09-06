from tkinter import *
root=Tk()
frame1=Frame(root,width=100,heigh=100,bg='green',bd=3)
# Свойство bd отвечает за расстояние от края рамки до виджетов.
frame2=Frame(root,bg='red',bd=3)
button1=Button(frame1,text='Первая кнопка')
button2=Button(frame2,text='Вторая кнопка')
frame1.pack()
frame2.pack()
button1.pack()
button2.pack()
root.mainloop()

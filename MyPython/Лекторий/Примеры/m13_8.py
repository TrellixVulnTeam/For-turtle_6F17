from tkinter import *
root=Tk()
button1 = Button(text="Левая",bg = 'Red')
button2 = Button(text="Верх", bg = 'orange')
button3 = Button(text="Низ",bg = 'Yellow')
button4 = Button(text="Право", bg = 'Green')

button1.place(x=45,y=0, bordermode='inside',
              width = 80, height=30 )
button2.place(x=0,y=40, bordermode = 'outside',
              width = 80, height=30)
button3.place(x=90,y=40, bordermode = 'outside',
              width = 80, height=30)
button4.place(x=45,y=80, bordermode = 'ignore',
              width = 80, height=30)
root.mainloop()

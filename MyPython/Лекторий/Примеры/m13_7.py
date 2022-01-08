from tkinter import *
root=Tk()
button1 = Button(text="Левая", bg = 'Red')
button2 = Button(text="Верх", bg = 'orange')
button3 = Button(text="Низ",bg = 'Yellow')
button4 = Button(text="Право", bg = 'Green')

button1.grid(row=0,column=0, columnspan = 2)
button2.grid(row=0,column=2, columnspan = 2)
button3.grid(row=0,column=4, columnspan = 2)
button4.grid(row=0,column=6, columnspan = 2)
root.mainloop()

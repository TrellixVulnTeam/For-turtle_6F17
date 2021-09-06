from tkinter import *
root=Tk()
text1=Text(root,height=7,width=7,
           font='Arial 14',wrap=WORD)
but = Button(root,text = 'Сохранить')
text1.pack()
but.pack()
root.mainloop()

from tkinter import *
def hide_show():
    label.destroy()
    
root=Tk()
label = Label(text='Я здесь!')
label.grid()
button = Button(command=hide_show, text="Cпрятать")
button.grid()
root.mainloop()

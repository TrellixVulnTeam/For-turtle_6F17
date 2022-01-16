from tkinter import *
def calc_add(event):
    num1 = int(ent_1.get())
    num2 = int(ent_2.get())
    lab['text'] = f'{num1 + num2}'

def calc_sub(event):
    num1 = int(ent_1.get())
    num2 = int(ent_2.get())
    lab['text'] = f'{num1 - num2}'

def calc_mul(event):
    num1 = int(ent_1.get())
    num2 = int(ent_2.get())
    lab['text'] = f'{num1 * num2}'

def calc_div(event):
    num1 = int(ent_1.get())
    num2 = int(ent_2.get())
    lab['text'] = f'{num1 / num2}'

root = Tk()
ent_1 = Entry(width=20)
ent_2 = Entry(width=20)

but_add = Button(text="+", width=10)
but_sub = Button(text="-", width=10)
but_mul = Button(text="*", width=10)
but_div = Button(text="/", width=10)

lab = Label(width=20)

but_add.bind('<Button-1>', calc_add)
but_sub.bind('<Button-1>', calc_sub)
but_mul.bind('<Button-1>', calc_mul)
but_div.bind('<Button-1>', calc_div)



ent_1.pack()
ent_2.pack()

but_add.pack()
but_sub.pack()
but_mul.pack()
but_div.pack()

lab.pack()

root.mainloop()
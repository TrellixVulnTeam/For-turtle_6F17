from tkinter import *
#ex.txt
window = Tk()

def open_file():
    name = ent.get()
    file = open(name, "r", encoding="utf-8")
    string = 1.0
    for i in file:
        text.insert(string, i)
        string += 1
    file.close()


def save_file():
    name = ent.get()
    file = open(name, "w", encoding="utf-8")
    string = 1.0

    aux = text.get(string, END).split('\n')
    for i in aux:
        file.write(i+'\n')

    file.close()

frame1 = Frame(window)
ent = Entry(frame1, width=20)
but_open = Button(frame1, text='Open', width=10, command=open_file)
but_save = Button(frame1, text='Save', width=10, command=save_file)

frame2 = Frame(window)
text = Text(frame2, width=40, wrap=WORD)
scroll_y = Scrollbar(frame2, command=text.yview, orient=VERTICAL)
scroll_x = Scrollbar(frame2, command=text.xview, orient=HORIZONTAL)

frame1.pack(padx=5, pady=5)
ent.pack(side=LEFT, padx=5)
but_open.pack(side=LEFT)
but_save.pack(side=LEFT)

frame2.pack()
scroll_x.pack(side=BOTTOM, fill=X, anchor=W)
text.pack(side=LEFT, padx=5, pady=5)
scroll_y.pack(side=LEFT, fill=Y)

text.config(yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)


window.mainloop()

from tkinter import *
import time
def tick():
    label.after(200, tick)
    # через каждые 200 миллисекунд обращаться к функции
    label['text'] = time.strftime('%H:%M:%S')
    # выводим время
root=Tk()
label = Label(font='sans 20')
label.pack()
label.after_idle(tick)
# после всех действий идет обращение к tick
root.mainloop()

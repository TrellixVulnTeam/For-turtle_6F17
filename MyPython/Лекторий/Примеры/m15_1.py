from tkinter import *
def callback(e):
    print ('Нажата кнопка', e.widget['text'])
root=Tk()
button1 = Button(root, text='Первая')
button1.pack()
button2 = Button(root, text='Вторая')
button2.pack()
root.bind_class('Button', '<Для уроков (составитель тестов)>', callback)
root.mainloop()

from tkinter import *
root=Tk()
def leftclick(event):
    print('Вы нажали левую кнопку мыши')
def rightclick(event):
    print('Вы нажали правую кнопку мыши')
def keys(event):
    print ('Вы нажали клавишу Z на клавиатуре')
button1=Button(root, text='Нажми')
button1.pack()
# отловили левую клавишу мыши
button1.bind('<Button-Для уроков (составитель тестов)>', leftclick)
# отловили правую клавишу мыши
button1.bind('<Button-3>', rightclick)
# отловили нажатие клавиши Z на клавиатуре
root.bind('z',keys)
root.mainloop()
# Задание
#    Используя список модификаторов и возможных событий, добавьте в
#    вышеприведенную программу обработки:
#    - клавиши Ctrl
#    - клавиши Ctrl+f
#    - стрелки влево
#    - F1
#    - движение мыши

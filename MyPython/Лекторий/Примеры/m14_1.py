from tkinter import *
import time
def button_clicked():
    # изменяем текст кнопки
    button['text'] = time.strftime('%H:%M:%S')
    # strftime - метод, который преобразует текущее время в строку 
root=Tk()
button = Button(root)
# конфигурируем виджет после создания
button.configure(text=time.strftime('%H:%M:%S'), command=button_clicked)
# также можно использовать квадратные скобки:
# button['text'] = time.strftime('%H:%M:%S')
# button['command'] = button_clicked
button.pack()
root.mainloop()
# функция button_clicked вызывается после щелчка по кнопке.

# Задание
#    Измените данную программу так, чтобы помимо времени
#    программа выводила еще год, месяц и год.

#    Возможно, вам понадобится дополнительная информация о
#    модуле Time. Кое-что можно узнать из Интернета, кое-что
#    из файла Комплекс для студентов Python\Теория для студентов\Модуль Time    

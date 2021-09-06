from tkinter import *
root=Tk()
listbox1=Listbox(root,height=5,width=20,selectmode=EXTENDED)
# в listbox1 можно выбирать любое количество элементов
listbox2=Listbox(root,height=5,width=20,selectmode=SINGLE)
# в listbox2 можно выбирать только одни элемент
list1=["Москва","Санкт-Петербург","Саратов","Омск"]
list2=["Канберра","Сидней","Мельбурн","Аделаида"]
# занесение списка в listbox1
for i in list1:
    listbox1.insert(END,i)
# занесение списка в listbox2
for i in list2:
    listbox2.insert(END,i)
listbox1.pack()
listbox2.pack()
root.mainloop()
# Задание
#    Добавьте в программу третий список (Listbox).
#    Попробуйте вывести окна с виджетом в ряд
#    (возможно, с помощью другого упаковщика)

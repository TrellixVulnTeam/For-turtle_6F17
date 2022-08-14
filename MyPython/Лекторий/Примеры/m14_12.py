from tkinter import *
# создаем холст, у которого задаем размер и цвет 
c = Canvas(width=460,height=100,bg='grey80')
c.pack()

# создаем три объекта: овал, прямоугольник и многоугольник (треугольник)
 
oval = c.create_oval(30,10,130,80,fill="orange")
c.create_rectangle(180,10,280,80,tag="rect",fill="lightgreen")
trian = c.create_polygon(330,80,380,10,430,80,fill='white',outline="black")

# создаем три процедуры, которые работают с созданными объектами
 
def oval_func(event):
# эта процедура убирает овал и выводит текст 
     c.delete(oval)
     c.create_text(30,10,text="Здесь был круг",anchor="w")
     
def rect_func(event):
# эта процедура убирает прамоугольник и выводит текст 
     c.delete("rect")
     c.create_text(180,10,text="Здесь был\nпрямоугольник",anchor="nw")
     
def triangle(event):
# эта процедура внутри многоугольника рисует желтый треугольник 
     c.create_polygon(350,70,380,20,410,70,fill='yellow',outline="black")

# Метод tag_bind позволяет привязать событие (например, щелчок кнопкой мыши)
# к определенному объекту. Таким образом, можно hеализовать обращение к
# различным областям холста с помощью одного и того же события.
# Пример ниже это наглядно иллюстрирует: изменения на холсте зависят
# от того, где произведен щелчок мышью.

c.tag_bind(oval,'<Button-Для уроков (составитель тестов)>',oval_func)
c.tag_bind("rect",'<Button-Для уроков (составитель тестов)>',rect_func)
c.tag_bind(trian,'<Button-Для уроков (составитель тестов)>',triangle)
 
mainloop() 

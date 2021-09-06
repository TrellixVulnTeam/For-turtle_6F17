from math import * #Вызов из библиотеки функций математики
from turtle import * #Вызов из библиотеки Чепепаха всех функций
shape('turtle') # задание формы маркера turtle = черепаха
penup() # поднять перо
pendown() # опустить перо
def krug(R = 200, s = "#000000"):
    """ Функция рисования круга с радиусом R и цветом C
    Цвет задаётся либо названием, либо в диапазрне RGB #000000 - #FFFFFF
    Круг рисуется таким образом, что черепаха находится в центре круга
    Возращается в туже точку
    """
    penup() # выход на точку окружности
    forward(R)
    pendown()
    left(90)
    

    # коэффициент качесчтва
    a = 2 * R * sin(0.5*pi/180)# вычисление длинны шага a

    fillcolor(s)# устанавливаем цвет заливки
    begin_fill()#начало фигуры для заливки 
    for i in range (360): # отрировка круга
        forward(a)
        left(1)
    end_fill()# конец фигуры для заливки
    
    penup() # возврат в исходную точку
    right(90) 
    backward(R)
    
def smile():
    krug(400,"yellow") # тело

    left((180-60)/2)# глаза
    forward(300)
    krug(30,"blue")
    left(120)
    forward(300)
    krug(30,"blue")
    home()

    left(90) # нос
    pensize(20)
    color("gray")
    pendown()
    forward(45)
    penup()
    home()

    pensize(35)# рот
    forward(300)
    right(90)
    color("red")
    a = 2 * 300 * sin(0.5*pi/180)
    pendown()
    for i in range (180): # отрировка круга
        forward(a)
        right(1)

smile()

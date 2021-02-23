import turtle
import math


def ex1():
    turtle.penup()
    turtle.setx(-300)
    n = 10
    size = 30

    def square(side):
        turtle.pendown()
        for j in range(4):
            turtle.forward(side)
            turtle.left(90)
        turtle.penup()

    for i in range(n):
        square(size)
        turtle.forward(2 * size)

    turtle.done()


def ex2():
    turtle.penup()
    turtle.setx(-300)
    n = 20
    size = 40

    def square(side):
        turtle.pendown()
        for j in range(4):
            turtle.forward(side)
            turtle.left(90)
        turtle.penup()

    for i in range(n):
        square(size * (-1)**i)
        turtle.forward(0 if i % 2 == 0 else 2 * size)

    turtle.done()


def ex3():
    turtle.setx(-300)
    n = 20
    size = 50
    angle1 = math.atan(1 / 2) * 180 / math.pi  # угол поворота для поска точки начала отрисовки ромба
    dig1 = (size ** 2 + (size / 2) ** 2) ** 0.5  # расстояние до точки начала отрисовки ромба
    dig2 = size * 2**0.5  # угол поворота для поска точки начала отрисовки квадрата на исходной линии рисунка
    angle2 = math.atan(size / 2 / dig2) * 180 / math.pi  # расстояние для перехода отрисовки квадрата на исходной линии

    def square(side):
        turtle.pendown()
        for j in range(4):
            turtle.forward(side)
            turtle.left(90)
        turtle.penup()

    for i in range(n):
        square(size)
        if i % 2 == 0:
            turtle.left(angle1)
            turtle.forward(dig1)
            turtle.left(-45 - angle1)
        else:
            turtle.left(45 - angle2)
            turtle.forward(((size / 2)**2 + dig2**2)**0.5)
            turtle.left(angle2)

    turtle.done()


def ex4():
    n = 10
    base = 20  # базовый размер элемента орнамента
    turtle.setx(-300)

    def ornament_left(size):
        turtle.pendown()
        small = size
        big = size * 3 / 2

        for angle, step in ((90, big), (90, small), (-90, small), (-90, small), (0, big)):
            turtle.forward(step)
            turtle.left(angle)
        turtle.penup()

    def ornament_right(size):
        turtle.pendown()
        small = size
        big = size * 3 / 2
        for angle, step in ((-90, big), (-90, small), (+90, small), (+90, small), (0, big)):
            turtle.forward(step)
            turtle.left(angle)
        turtle.penup()

    for i in range(n):
        ornament_left(base)
        ornament_right(base)

    turtle.done()


def ex5():
    n = 10
    base = 50  # базовый размер элемента орнамента
    turtle.setx(-300)

    def ornament_right(size):
        turtle.pendown()

        small = size
        for j in range(6):
            turtle.forward(small)
            small = size - size / 5 * j
            turtle.right(90)
        turtle.penup()

    def ornament_left(size):
        turtle.pendown()
        small = size / 5

        for j in range(5):
            turtle.forward(small)
            small += size / 5
            turtle.left(90)
        turtle.penup()

    turtle.left(90)
    for i in range(n):
        ornament_right(base)
        turtle.pendown()
        turtle.forward(base / 5)
        turtle.left(90)
        ornament_left(base)

    turtle.done()


def ex6():
    n = 10
    base = 30  # базовый размер элемента орнамента
    turtle.setx(-300)

    def ornament_right(size):
        turtle.pendown()

        for j in range(2):
            turtle.circle(-size, 180)
            size /= 3
        turtle.penup()

    def ornament_left(size):
        turtle.pendown()
        small = size / 3
        for j in range(2):
            turtle.circle(small, 180)
            small = size
        turtle.penup()

    turtle.left(90)
    for i in range(n):
        ornament_right(base)
        ornament_left(base)

    turtle.done()


def ex7():
    n = 10
    base = 50
    turtle.setx(-300)

    def zig_zag(size):
        turtle.pendown()
        turtle.forward(size / 2)
        turtle.left(90)
        turtle.forward(size)
        turtle.left(-90)
        turtle.forward(size)
        turtle.left(-90)
        turtle.forward(size / 2)
        turtle.left(-90)
        turtle.forward(size / 2)
        turtle.left(90)
        turtle.forward(size / 2)
        turtle.left(90)
        turtle.forward(size / 2)
        turtle.penup()

    for i in range(n):
        zig_zag(base)

    turtle.done()


def ex8():

    turtle.done()


def control(ex):
    turtle.hideturtle()
    turtle.speed(0)
    turtle.penup()
    if ex == 1:
        ex1()
    elif ex == 2:
        ex2()
    elif ex == 3:
        ex3()
    elif ex == 4:
        ex4()
    elif ex == 5:
        ex5()
    elif ex == 6:
        ex6()
    elif ex == 7:
        ex7()
    elif ex == 8:
        ex8()


if __name__ == "__main__":
    quiz = int(input("""Выберите задание:
     1. Линия квадратов
     2. Двойная линия квадратов
     3. Линия из ромбов и квадратов
     4. Орнамент "Т"
     5. Орнамент Квадратная волна
     6. Орнамент Волна
     7. Орнамент Простая волна
     8. Орнамент по кругу
    Ответ: """))
    control(quiz)

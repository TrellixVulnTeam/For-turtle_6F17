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
    angle1 = math.atan(1 / 2) * 180 / math.pi
    dig1 = (size ** 2 + (size / 2) ** 2) ** 0.5
    dig2 = size * 2**0.5
    angle2 = math.atan(size / 2 / dig2) * 180 / math.pi

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
    base = 20
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
    base = 20
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


def ex6():

    turtle.done()


def ex7():

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

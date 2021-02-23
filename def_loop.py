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
    turtle.penup()
    turtle.setx(-300)
    n = 20
    size = 30
    angle1 = math.atan(1 / 2) * 180 / math.pi
    dig1 = (size ** 2 + (size / 2) ** 2) ** 0.5

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
            turtle.left(45)
            turtle.forward(math.sqrt(2) * size)
            turtle.left(90)
            turtle.backward(size / 2)
            turtle.left(-90)

    turtle.done()


def ex4():

    turtle.done()


def ex5():

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

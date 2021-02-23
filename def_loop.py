import turtle
import math


def ex1():

    turtle.done()


def ex2():

    turtle.done()


def ex3():

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

import turtle
import math


def ex1():
    pass


def ex2():
    pass


def ex3():
    pass


def ex4():
    pass


def ex5():
    pass


def ex6():
    pass


def ex7():
    pass


def ex8():
    pass


def ex9():
    pass


def ex10():
    pass


def ex11():
    pass


def ex12():
    pass


def ex13():
    pass


def ex14():
    pass


def ex15():
    pass


def ex16():
    pass


def ex17():
    pass


def ex18():
    pass


def ex19():
    pass


def ex20():
    pass


def ex21():
    pass


def ex22():
    pass


def ex23():
    pass


def ex24():
    pass


def ex25():
    def spiral(start_line, start):
        '''

        :param start_line:
        :param start:
        :return:
        '''
        while start_line >= start:
            turtle.forward(start_line)
            turtle.left(90)
            start_line = start_line - 2 * start
        turtle.forward(2 * start)
        while start_line < a - 2 * start:
            start_line = start_line + 2 * start
            turtle.left(-90)
            turtle.forward(start_line)

    n = 4  # Число витков
    a = 500  # сторона квадрата
    turtle.speed(0)  # Скорость черепахи

    for i in range(4):
        turtle.forward(a)
        turtle.left(90)

    start = a / (2 ** (n + 1))
    start_line = start * (2 ** (n + 1) - 2)
    # стартовая позиция для 1-й спирали
    turtle.left(90)
    turtle.forward(start)
    turtle.left(-90)

    spiral(start_line, start)
    # стартовая позиция для 2-й спирали
    turtle.left(-90)
    turtle.forward(a - start)
    turtle.left(-90)
    turtle.forward(start)
    turtle.left(-90)

    spiral(start_line, start)


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
    elif ex == 9:
        ex9()
    elif ex == 10:
        ex10()
    elif ex == 11:
        ex11()
    elif ex == 12:
        ex12()
    elif ex == 13:
        ex13()
    elif ex == 14:
        ex14()
    elif ex == 15:
        ex15()
    elif ex == 16:
        ex16()
    elif ex == 17:
        ex17()
    elif ex == 18:
        ex18()
    elif ex == 19:
        ex19()
    elif ex == 20:
        ex20()
    elif ex == 21:
        ex21()
    elif ex == 22:
        ex22()
    elif ex == 23:
        ex23()
    elif ex == 24:
        ex24()
    elif ex == 25:
        ex25()


if __name__ == "__main__":
    quiz = int(input("""Выберите задание:
    25. Спираль в квадрате
    Ответ: """))
    control(quiz)

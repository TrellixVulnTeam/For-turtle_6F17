import turtle
#import math


def ex1():
    a = 20
    b = a / 4
    steps = 25

    for i in range(steps):
        turtle.forward(a)
        turtle.left(90)
        turtle.forward(b)
        turtle.right(90)
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


def ex9():
    turtle.done()


def ex10():
    turtle.done()


def ex11():
    turtle.done()


def ex12():
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
    elif ex == 9:
        ex9()
    elif ex == 10:
        ex10()
    elif ex == 11:
        ex11()
    elif ex == 12:
        ex12()


if __name__ == "__main__":
    quiz = int(input("""Выберите задание:
     1. Лесенка
     2. Частокол
     3. Прямоугольный забор
     4. "Кремлёвский" забор
     5. Треугольный забор
     6. Профиль
     7. Дуговой забор
     8. Правльные многоугольники
     9. Простой крест
    10. Крест из квадратов
    11. Веер из квадратов
    12. Платочки
    13. Цветок из треугольников
    14. Наутилус из треугольников
    15. Чветок circle()
    16. Спираль с постоянным шагом
    17. Прямоугольный забор
    18. Пирамида треугольников
    19. 4 лепестка
    20. Четырехлистрик
    21. Ромашка
    Ответ: """))
    control(quiz)

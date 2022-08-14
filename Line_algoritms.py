import turtle
import math


def ex1():
    pen = 3
    size = 100

    turtle.pensize(pen)
    turtle.left(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size / 2)
    turtle.right(90)
    turtle.forward(size / 2)
    turtle.left(90)
    turtle.forward(size / 2)
    turtle.left(90)
    turtle.forward(size / 2)
    turtle.right(90)
    turtle.forward(size / 2)
    turtle.right(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size / 3)
    turtle.done()


def ex2():
    pen = 1
    size_h = 100

    size_v = size_h / 3 * 4
    turtle.pensize(pen)
    turtle.forward(size_h)
    turtle.left(90)
    turtle.forward(size_v)
    turtle.left(90)
    turtle.forward(size_h)
    turtle.left(90)
    turtle.forward(size_v)
    turtle.left(90)
    turtle.forward(size_h / 2)
    turtle.left(90)
    turtle.forward(size_v / 3 * 2)
    turtle.left(90)
    turtle.forward(size_h / 2)
    turtle.backward(size_h)
    turtle.done()


def ex3():
    pen = 1
    size = 300

    turtle.pensize(pen)
    turtle.begin_fill()
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size / 2)
    turtle.left(135)
    turtle.forward(size * 2 ** 0.5)
    turtle.left(-135)
    turtle.forward(size / 2)
    turtle.end_fill()
    turtle.done()


def ex4():
    pen = 1
    size = 100

    turtle.pensize(pen)
    turtle.begin_fill()
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.end_fill()
    turtle.done()


def ex5():
    pen = 1
    size_a = size_b = size_c = 100
    angle = 45

    turtle.pensize(pen)
    turtle.left(angle)
    turtle.forward(size_a)
    turtle.left(90 - angle)
    turtle.forward(size_b)
    turtle.left(90 - angle)
    turtle.forward(size_c)
    turtle.left(angle * 2)
    turtle.forward(size_a)
    turtle.left(90 - angle)
    turtle.forward(size_b)
    turtle.left(90 - angle)
    turtle.forward(size_c)
    turtle.left(90 + angle)
    turtle.forward(size_b)
    turtle.left(90 - angle)
    turtle.forward(size_c)
    turtle.backward(size_c)
    turtle.right(180 - 2 * angle)
    turtle.forward(size_a)
    turtle.done()


def ex6():
    pen = 1
    size_a = 200
    size_b = 300
    size_c = 100
    angle = 35

    def box(a, b, c, ang):
        turtle.left(ang)
        turtle.forward(a)
        turtle.left(90 - ang)
        turtle.forward(b)
        turtle.left(90 - ang)
        turtle.forward(c)
        turtle.left(ang * 2)
        turtle.forward(a)
        turtle.left(90 - ang)
        turtle.forward(b)
        turtle.left(90 - ang)
        turtle.forward(c)
        turtle.left(90 + ang)
        turtle.forward(b)
        turtle.left(90 - ang)
        turtle.forward(c)
        turtle.backward(c)
        turtle.right(180 - 2 * ang)
        turtle.forward(a)

    box(size_a, size_b, size_c, angle)

    turtle.penup()
    turtle.width(pen)
    turtle.goto(size_b * 1.5, 0)
    turtle.left(-turtle.heading())
    angle -= 20
    turtle.pendown()

    box(size_b, size_c, size_a, angle)

    turtle.done()


def ex7():
    pen = 1
    size = 300

    turtle.pensize(pen)
    turtle.forward(size)
    turtle.left(120)
    turtle.forward(size)
    turtle.left(120)
    turtle.forward(size)
    turtle.left(120)
    turtle.forward(size / 2)
    turtle.left(90)
    bis = size * 3 ** 0.5 / 2
    turtle.forward(bis)
    turtle.left(150)
    turtle.forward(size / 2)
    turtle.left(90)
    turtle.forward(bis)
    turtle.left(150)
    turtle.forward(size / 2)
    turtle.left(90)
    turtle.forward(bis)

    turtle.done()


def ex8():
    pen = 1
    size = 300

    turtle.pensize(pen)
    turtle.forward(size)
    turtle.left(120)
    turtle.forward(size)
    turtle.left(120)
    turtle.forward(size)
    turtle.left(120)
    turtle.forward(size / 2)
    turtle.left(60)
    turtle.forward(size / 2)
    turtle.left(120)
    turtle.forward(size / 2)
    turtle.left(120)
    turtle.forward(size / 2)
    turtle.done()


def ex9():
    pen = 1
    size = 2

    turtle.pensize(pen)
    turtle.left(90)
    for i in range(180):
        turtle.forward(size)
        turtle.left(1)
    turtle.done()


def ex10():
    pen = 1
    size = 2

    turtle.pensize(pen)
    turtle.left(-90)

    def arc(r, n=1):
        for i in range(180):
            turtle.forward(r)
            turtle.left(1 * n)

    arc(size, -1)
    arc(size / 2, -1)
    arc(size / 2)
    arc(size)

    turtle.done()


def ex11():
    pen = 1
    size = 100

    turtle.pensize(pen)

    def kv(a, n=1):
        for i in range(5):
            turtle.forward(a)
            turtle.left(90 * n)

    kv(size)
    turtle.right(45)
    kv(size / 2 ** 0.5, -1)
    turtle.left(180)
    kv(size / 2 ** 0.5, -1)
    turtle.done()


def ex12():
    pen = 1
    base_size = 200
    angle = 45

    turtle.pensize(pen)

    def kv(a, n=1):
        for i in range(5):
            turtle.forward(a)
            turtle.left(90 * n)

    kv(base_size)

    turtle.right(90 - angle)

    kv(base_size * math.sin(math.pi * angle / 180), -1)

    turtle.left(180)

    kv(base_size * math.cos(math.pi * angle / 180), -1)

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
     Для уроков (составитель тестов). Кривая
     2. Окно
     3. Бант
     4. Квадрат
     5. Куб
     6. Кирпичики
     7. Треугольник-Для уроков (составитель тестов)
     8. Треугольник-2
     9. Дуга
    10. Дзен
    11. Пифагоровы штаны-Для уроков (составитель тестов)
    12. Пифагоровы штану-2
    Ответ: """))
    control(quiz)

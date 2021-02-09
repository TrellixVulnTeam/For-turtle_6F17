import turtle


def begin():
    turtle.penup()
    turtle.setx(-450)
    turtle.pendown()


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
    a = 30
    b = a * 1
    steps = 20

    for i in range(steps):
        turtle.left(90)
        turtle.forward(a)
        turtle.backward(a)
        turtle.right(90)
        turtle.forward(b)

    turtle.done()


def ex3():
    a = 20
    b = a * 1
    steps = 12

    def tr(ar, br):
        turtle.left(90)
        turtle.forward(ar)
        turtle.right(90)
        turtle.forward(br)

    def tl(al, bl):
        turtle.right(90)
        turtle.forward(al)
        turtle.left(90)
        turtle.forward(bl)

    for i in range(steps):
        tr(a, b)
        tl(a, b)

    turtle.done()


def ex4():
    a = 20
    b = 2 ** (1/2) * a
    steps = 12

    def tr(ar, br):
        turtle.left(90)
        turtle.forward(ar)
        turtle.right(135)
        turtle.forward(br)
        turtle.left(90)
        turtle.forward(br)
        turtle.right(45)

    def tl(al):
        bl = al
        turtle.right(90)
        turtle.forward(al)
        turtle.left(90)
        turtle.forward(bl)

    for i in range(steps):
        tr(a, b / 2)
        tl(a)

    turtle.done()


def ex5():
    a = 30
    steps = 12

    add_angle = 0
    turtle.left(45 + add_angle / 2)

    for i in range(steps):
        turtle.forward(a)
        turtle.right(90 + add_angle)
        turtle.forward(a)
        turtle.left(90 + add_angle)

    turtle.done()


def ex6():
    a = 30
    steps = 12

    add_angle = 0
    turtle.left(60 + add_angle)

    def tr(ar, angle):
        turtle.forward(ar)
        turtle.right(60 + angle)
        turtle.forward(ar)
        turtle.right(60 + angle)

    def tl(al, angle):
        turtle.forward(al)
        turtle.left(60 + angle)
        turtle.forward(al)
        turtle.left(60 + angle)

    for i in range(steps):
        tr(a, add_angle)
        tl(a, add_angle)

    turtle.done()


def ex7():
    r = 30
    steps = 12
    turtle.left(90)

    for i in range(steps):
        turtle.circle(-r, 180)
        turtle.left(180)

    turtle.done()


def ex8():
    a = 30
    steps = 10
    turtle.left(90)
    
    for i in range(3, steps):
        for j in range(i):
            turtle.forward(a)
            turtle.right(360 / i)
        turtle.penup()
        turtle.setx(turtle.xcor() + a * i / 2)
        turtle.pendown()

    turtle.done()


def ex9():
    a = 100
    turtle.left(90)

    for i in range(4):
        turtle.forward(a)
        turtle.right(90)
        turtle.forward(a)
        turtle.left(90)
        turtle.forward(a)
        turtle.left(90)

    turtle.done()


def ex10():
    a = 50
    turtle.left(90)

    for i in range(4):
        for j in range(5):
            turtle.forward(a)
            turtle.left(90)
        turtle.right(180)

    turtle.done()


def ex11():
    a = 100
    n = 3
    angle = 90 / (n + 1)
    turtle.left(angle)

    for i in range(n):
        for j in range(4):
            turtle.forward(a)
            turtle.left(90)
        turtle.left(angle)

    turtle.done()


def ex12():
    a = 150
    n = 2
    angle = 90 / n
    turtle.left(angle)

    for i in range(n):
        for j in range(4):
            for y in range(4):
                turtle.forward(a)
                turtle.right(90)
            turtle.right(90)
        turtle.right(angle)

    turtle.done()


def ex13():
    a = 150
    n = 5
    turtle.left(90)

    for i in range(n):
        for j in range(3):
            turtle.forward(a)
            turtle.right(120)
        turtle.left(360 / n)

    turtle.done()


def ex14():
    a = 300
    n = 720
    k = 7
    delta = 150 / n * (k - 2)
    turtle.left(90)

    for j in range(n // k):
        for i in range(3):
            turtle.forward(a)
            turtle.right(120)
        turtle.right(360 / n * k)
        a -= delta

    turtle.done()


def ex15():
    r = 100
    n = 8

    for i in range(n):
        turtle.circle(r)
        turtle.left(360 / n)

    turtle.done()


def ex16():
    turtle.done()


def ex17():
    turtle.done()


def ex18():
    turtle.done()


def ex19():
    turtle.done()


def ex20():
    turtle.done()


def ex21():
    turtle.done()


def control(ex):
    turtle.hideturtle()
    turtle.speed(0)
    if ex == 1:
        begin()
        ex1()
    elif ex == 2:
        begin()
        ex2()
    elif ex == 3:
        begin()
        ex3()
    elif ex == 4:
        begin()
        ex4()
    elif ex == 5:
        begin()
        ex5()
    elif ex == 6:
        begin()
        ex6()
    elif ex == 7:
        begin()
        ex7()
    elif ex == 8:
        begin()
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
    else:
        print("Такого задания нет")


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

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
     1. Кривая
     2. Окно
     3. Бант
     4. Квадрат
     5. Куб
     6. Кирпичики
     7. Треугольник-1
     8. Треугольник-2
     9. Дуга
    10. Дзен
    11. Пифагоровы штаны-1
    12. Пифагоровы штану-2
    Ответ: """))
    control(quiz)

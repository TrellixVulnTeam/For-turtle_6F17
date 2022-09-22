import turtle


def circle(R):
    turtle.left(90)
    turtle.circle(-R)
    turtle.right(90)


def pascal_tree(x, a):
    """
    :param x: глубина рекурсии
    :param a: длинна ветки дерева Паскаля на каждом из уровнкй
    :return: None
    """
    turtle.forward(a)
    if x > 0:
        aux1 = 0
        aux2 = 0.73
        turtle.left(45 + aux1)
        pascal_tree(x - 1, a * aux2)
        turtle.right(45 + aux1)
        pascal_tree(x - 1, a * aux2)
        turtle.right(45 + aux1)
        pascal_tree(x - 1, a * aux2)
        turtle.left(45 + aux1)
    if x == 0:
        circle(a // 4)
    turtle.backward(a)


turtle.left(90)
n = 7
size = 200
turtle.sety(-300)
turtle.speed(0)
pascal_tree(n, size)

turtle.done()

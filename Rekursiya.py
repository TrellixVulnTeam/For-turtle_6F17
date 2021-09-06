import turtle


def pascal_tree(x, a):
    """
    :param x: глубина рекурсии
    :param a: длинна ветки дерева Паскаля на каждом из уровнкй
    :return: None
    """
    turtle.forward(a)
    if x > 0:
        turtle.left(45)
        pascal_tree(x-1, a * 0.75)
        turtle.right(90)
        pascal_tree(x - 1, a * 0.75)
        turtle.left(45)
    turtle.backward(a)

turtle.left(90)
n = 10
size = 300
turtle.sety(-300)
pascal_tree(n, size)

turtle.done()

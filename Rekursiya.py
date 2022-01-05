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
        turtle.left(45)
        pascal_tree(x-1, a * 0.75)
        turtle.right(45)
        pascal_tree(x - 1, a * 0.75)
        turtle.right(45)
        pascal_tree(x - 1, a * 0.75)
        turtle.left(45)
    if x ==0:
        circle(a//4)
    turtle.backward(a)


turtle.left(90)
n = 10
size = 200
turtle.sety(-300)
turtle.speed(0)
pascal_tree(n, size)


turtle.done()


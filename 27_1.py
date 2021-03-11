def enter():
    flag = True
    while flag:
        a, b = map(int, input("Введи 2 числа 0 < a < b ").split())
        if 0 < a < b:
            flag = False
    return a, b

def sqr(a, b):
    for i in range(a, b + 1):
        print(f'{i} * {i} = {i * i}')


sqr(*enter())
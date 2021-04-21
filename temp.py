def marteshka(n):
    if n != 1:
        print(f'Верх {n} мартёшки')
        marteshka(n-1)
        print(f'Низ {n} матрёшки')
    else:
        print('Матрёшечка')


marteshka(5)
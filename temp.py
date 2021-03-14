a = b = 0
while not (0 < a < b):
    a, b = map(int, input("Введи числа а и b, которые "
                      "удовлетворяют условию 0 < a < b ").split())


while a <= b:
    print(f'{a} * {a} = {a * a}')
    a += 1


for i in range(a, b + 1):
    print(f'{i} * {i} = {i * i}')

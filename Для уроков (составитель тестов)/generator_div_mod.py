import random as r


def simpl(a, b):
    if r.random() >= 0.5:
        return f'{a} // {b}', a // b
    else:
        return f'{a} % {b}', a % b


def duble_simpl(a, b, c):
    op1, val1 = simpl(a, b)
    op2, val2 = simpl(val1, c)
    return f'{op1} {" ".join(op2.split()[1:])}', val2


n = 6
count = 1

file = open('Вопросы.txt', 'w')
for i in range(n):
    op, val = simpl(r.randint(100, 200), r.randint(25, 75))
    file.write(f'{count}. Вычислите выражение {op}. Ответ: {val}' + '\n')
    count +=1
file.write('\n')
for i in range(n):
    op, val = duble_simpl(r.randint(100, 200), r.randint(50, 100), r.randint(5, 25))
    file.write(f'{count}. Вычислите выражение {op}. Ответ: {val}' + '\n')
    count += 1
file.write('\n')
for i in range(n):
    op, val = simpl(r.randint(1000, 10000), r.choice([10, 100, 1000, 10000]))
    file.write(f'{count}. Вычислите выражение {op}. Ответ: {val}' + '\n')
    count += 1
file.write('\n')
for i in range(n):
    op, val = duble_simpl(r.randint(10000, 100000), r.choice([10, 100, 1000, 10000]), r.choice([10, 100, 1000, 10000]))
    file.write(f'{count}. Вычислите выражение {op}. Ответ: {val}' + '\n')
    count += 1
file.write('\n')
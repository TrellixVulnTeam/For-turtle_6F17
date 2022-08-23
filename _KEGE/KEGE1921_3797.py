"""
(№3797) Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежит две кучи камней. Игроки ходят по очереди,
первый ход делает Петя. За один ход игрок может добавить в любую кучу один камень или добавить  в любую кучу столько
камней, сколько их в данный момент в другой куче. Игра завершается в тот момент, когда общее количество камней
в двух кучах становится не менее 80. Победителем считается игрок, сделавший последний ход. В начальный момент в первой
куче было 8 камней, а во второй – S камней, 1 ≤ S ≤ 71.
Ответьте на следующие вопросы:

Вопрос 1. Известно, что Ваня выиграл своим первым ходом после неудачного первого хода Пети. Назовите минимальное
значение S, при котором это возможно.

Вопрос 2. Найдите минимальное и максимальное значение S, при котором у Пети есть выигрышная стратегия, причём
одновременно выполняются два условия:
− Петя не может выиграть за один ход;
− Петя может выиграть своим вторым ходом независимо от того, как будет ходить Ваня.
Найденные значения запишите в ответе в порядке возрастания.

Вопрос 3. Найдите значение S, при котором одновременно выполняются два условия:
– у Вани есть выигрышная стратегия, позволяющая ему выиграть первым или вторым ходом при любой игре Пети;
– у Вани нет стратегии, которая позволит ему гарантированно выиграть первым ходом.
"""

#    1      2      3      4      5
#  start   П1     В1     П2      В2

#Q19
def f19(x, y, pos=1):
    if x + y >= wins and pos == 3: return True
    if x + y < wins and pos == 3: return False

    return f19(x + 1, y, pos + 1) or f19(x + y, y, pos + 1) or f19(x, y + 1, pos + 1) or f19(x, y + x, pos + 1)


#Q20
def f20(x, y, pos=1):
    if x + y >= wins and pos == 4: return True
    if x + y < wins and pos == 4: return False
    if x + y >= wins: return False

    if pos % 2 == 0:
        return f20(x + 1, y, pos + 1) and f20(x + y, y, pos + 1) and f20(x, y + 1, pos + 1) and f20(x, y + x, pos + 1)
    else:
        return f20(x + 1, y, pos + 1) or f20(x + y, y, pos + 1) or f20(x, y + 1, pos + 1) or f20(x, y + x, pos + 1)


#Q21
def f21(x, y, pos = 1):
    if x + y >= wins and (pos == 3 or pos == 5): return True
    if x + y < wins and pos == 5: return False
    if x + y >= wins: return False

    if pos % 2 == 1:
        return f21(x + 1, y, pos + 1) and f21(x + y, y, pos + 1) and f21(x, y + 1, pos + 1) and f21(x, y + x, pos + 1)
    else:
        return f21(x + 1, y, pos + 1) or f21(x + y, y, pos + 1) or f21(x, y + 1, pos + 1) or f21(x, y + x, pos + 1)


def f21minor(x, y, pos = 1):
    if x + y >= wins and pos == 3: return True
    if x + y < wins and pos == 3: return False
    if x + y >= wins: return False

    if pos % 2 == 1:
        return f21minor(x + 1, y, pos + 1) and f21minor(x + y, y, pos + 1) and f21minor(x, y + 1, pos + 1) and f21minor(x, y + x, pos + 1)
    else:
        return f21minor(x + 1, y, pos + 1) or f21minor(x + y, y, pos + 1) or f21minor(x, y + 1, pos + 1) or f21minor(x, y + x, pos + 1)


wins = 80
hip1 = 8
start = 1
stop = wins - hip1

print('-' * 10 + 'Q19' + '-' * 10)
for s in range(start, stop):
    if f19(s, hip1):
        print(s)
        break

print('-' * 10 + 'Q20' + '-' * 10)
for s in range(start, stop):
    if f20(s, hip1):
        print(s)

print('-' * 10 + 'Q21' + '-' * 10)
for s in range(start, stop):
    if f21(s, hip1):
        print(s)
    if f21minor(s, hip1):
        print(f'minor {s}')
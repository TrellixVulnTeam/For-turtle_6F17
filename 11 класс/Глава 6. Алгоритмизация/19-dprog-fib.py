# -*- coding: utf-8 -*-
"""
 Программа к учебнику информатики для 11 класса
 К.Ю. Полякова и Е.А. Еремина.
 Глава 6.
 Программа № 19. Динамическое программирование.
                 Числа Фибоначчи
"""


def Fib(N):
    if N < 3: return 1
    return Fib(N - 1) + Fib(N - 2)


import time

N = 35

print(f"Вычисляется F({N:d}) ...")
t0 = time.perf_counter()
FN = Fib(N)
dt = time.perf_counter() - t0
print("Рекурсивная функция:")
print(f"  F({N}) = {FN}, время {dt:0.8f} c")

t0 = time.perf_counter()
F = [1] * (N + 1)
for i in range(3, N + 1):
    F[i] = F[i - 1] + F[i - 2]
FN = F[N]
dt = time.perf_counter() - t0
print("Итерация с хранением данных в массиве:")
print(f"  F({N}) = {FN}, время {dt:0.8f} c")

t0 = time.perf_counter()
f2 = f1 = fN = 1
for i in range(3, N + 1):
    fN = f1 + f2
    f2 = f1
    f1 = fN
dt = time.perf_counter() - t0
print("Итерация без массива:")
print(f"  F({N}) = {FN}, время {dt:0.8f} c")

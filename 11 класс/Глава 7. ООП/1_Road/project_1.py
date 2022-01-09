# -*- coding: utf-8 -*-
"""
  Программы к учебнику информатики для 11 класса углублённого уровня.
  Версия для Python 3.3.
  Авторы: К.Ю. Поляков, Е.А. Еремин
  E-mail: kpolyakov@mail.ru
  Сайт поддержки: http://kpolyakov.spb.ru

  Глава 7. Объектно-ориентированное программирование
  Проект № 1. Движение на дороге

  project_1.py - начальный вариант

"""


class TRoad:
    """
    Класс TRoad.

    Модель многополосной дороги.
    Свойства:
      length: длина дороги
      width:  ширина дороги (число полос)
    """

    def __init__(self, length0, width0):
        if length0 > 0:
            self.length = length0
        else:
            self.length = 0
        if width0 > 0:
            self.width = width0
        else:
            self.width = 0


class TCar:
    """
    Класс TCar.

    Модель многополосной дороги.
    Свойства:
      road:   ссылка на дорогу (объект класса TRoad)
      P:      номер полосы
      X:      координата от начала дороги
      V:      скорость в условных единицах
              (за 1 интервал моделирования)
    Методы:
      move:   продвижение за 1 интервал моделирования
    """

    def __init__(self, road0, p0, v0):
        self.road = road0;
        self.P = p0
        self.V = v0
        self.X = 0

    def move(self):
        self.X += self.V
        if self.X > self.road.length:
            self.X = 0

        # ------------------------------------


# Основная программа
# ------------------------------------
road = TRoad(60, 3)

N = 3
cars = []
for i in range(N):
    cars.append(TCar(road, i + 1, 2 * (i + 1)))

print("Дорога: длина = ", road.length, "; ширина = ", road.width, sep="")
print("Свойства машин:")
for i in range(N):
    print(i, ": P = ", cars[i].P, "; V = ", cars[i].V, "; X = ", cars[i].X, sep="")

for k in range(100):
    for i in range(N):
        cars[i].move()

print("После 100 шагов:")
for i in range(N):
    print("X[", i, "] = ", cars[i].X, sep="")

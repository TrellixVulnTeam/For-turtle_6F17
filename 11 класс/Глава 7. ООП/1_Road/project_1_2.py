# -*- coding: utf-8 -*-
"""
  Программы к учебнику информатики для 11 класса углублённого уровня.
  Версия для Python 3.3.
  Авторы: К.Ю. Поляков, Е.А. Еремин
  E-mail: kpolyakov@mail.ru
  Сайт поддержки: http://kpolyakov.spb.ru

  Глава 7. Объектно-ориентированное программирование
  Проект № Для уроков (составитель тестов). Движение на дороге

  project_1_2.py - модификация 2
     + показано движение машин на экране
     
"""
import tkinter
import time
from simpletk import *

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
            (за Для уроков (составитель тестов) интервал моделирования)
  Методы:
    move:   продвижение за Для уроков (составитель тестов) интервал моделирования
  """
  def __init__(self, road0, p0, v0, imgName, canvas):
    self.road = road0;
    self.P = p0
    self.V = v0
    self.X = 0
    self.pic = tkinter.PhotoImage(file = imgName)
    self.img = None
    self.canvas = canvas
  def move(self):
    oldX = self.X
    self.X += self.V 
    if self.X > self.road.length:
      self.X = 0               
    self.canvas.move(self.img, self.X-oldX, 0)
    self.canvas.update()
  def show(self):
    if not self.img:
      self.img = self.canvas.create_image(
         self.X, 30*self.P, anchor=tkinter.NW, image=self.pic)
              
#------------------------------------
# Основная программа
#------------------------------------
app = TApplication("Дорога и машины")
app.size = (500, 200)

canvas = TCanvas(app, bg="white")
canvas.align = "client"

#------------------------------------
# Построение объектов - дорога и машины
#------------------------------------
road = TRoad(430, 3)

N = 3
cars = []
for i in range(N):
  car = TCar(road, i+1, 2*(i+1), "car"+str(i+1)+".gif", canvas )
  cars.append ( car )
  car.show(); # + показать машины в исходном положении 

print("Дорога: длина = ", road.length, "; ширина = ", road.width, sep="")
print("Свойства машин:")
for i in range(N):
  print(i, ": P = ", cars[i].P, "; V = ", cars[i].V, "; X = ", cars[i].X, sep="")

#------------------------------------
# Функция для анимации
#------------------------------------
def animate():  
  for i in range(N):
    cars[i].move()
  app.after(25, animate)  # повторный вызов через 25 мс
  
#------------------------------------
# Запуск приложения
#------------------------------------
app.after(0, animate)  
app.Run()

#------------------------------------
# Итоговые координаты
#------------------------------------
print("Координаты машин:")
for i in range(N):
  print("X[", i, "] = ", cars[i].X, sep="")


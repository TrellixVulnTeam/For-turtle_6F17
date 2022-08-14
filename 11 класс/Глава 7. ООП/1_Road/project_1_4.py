# -*- coding: utf-8 -*-
"""
  Программы к учебнику информатики для 11 класса углублённого уровня.
  Версия для Python 3.3.
  Авторы: К.Ю. Поляков, Е.А. Еремин
  E-mail: kpolyakov@mail.ru
  Сайт поддержки: http://kpolyakov.spb.ru

  Глава 7. Объектно-ориентированное программирование
  Проект № Для уроков (составитель тестов). Движение на дороге

  project_1_4.py - модификация 4
     + машины останавливаются перед светофором, если горит
       красный свет
     
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
    lights: список ссылок на светофоры
  Методы:
    nextLight: найти ближайший светофор
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
    self.lights = []
  def addLight(self, light):
    self.lights.append(light)
  def nextLight(self, X):
    light = None
    for lt in self.lights:
      if X < lt.X:
        if light == None or lt.X < light.X:
          light = lt
    return light
    
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
    w = self.pic.width()
    light = self.road.nextLight(self.X + w - 1)
    self.X += self.V 
    if light != None and light.state != TLight.green \
       and self.X + w > light.X:
      self.X = light.X - w
    if self.X > self.road.length:
      self.X = 0  
    self.canvas.move(self.img, self.X-oldX, 0)
    self.canvas.update()
  def show(self):
    if not self.img:
      self.img = self.canvas.create_image(
         self.X, 25+30*self.P, anchor=tkinter.NW, image=self.pic)
              
class TLight:
  """
  Класс TLight.

  Модель светофора. 
  Свойства:
    X:      координата от начала дороги
    state:  состояние (тип рисунка) 
  Методы:
    timeStep: продвижение за Для уроков (составитель тестов) интервал моделирования
  """
  red = 0 
  redYellow = 1
  green = 2
  yellow = 3
  def __init__(self, X, imgName, canvas):
    self.X = X
    self.pics = [None]*4
    for i in range(4):
      fName = imgName + str(i+1) + ".gif"
      self.pics[i] = tkinter.PhotoImage(file = fName)
    self.stateCounter = 0
    self.state = self.red
    self.canvas = canvas
    self.img = None
  def hide(self):
    if self.img:
      self.canvas.delete(self.img)
      self.img = None
  def show(self):
    if not self.img:
      self.img = self.canvas.create_image(
         self.X, 0, anchor=tkinter.NW, image=self.pics[self.state])
  def timeStep(self):
    prevState = self.state
    self.stateCounter += 1
    if self.stateCounter == 100: self.state = self.redYellow
    elif self.stateCounter == 120: self.state = self.green
    elif self.stateCounter == 220: self.state = self.yellow
    elif self.stateCounter == 240: 
      self.state = self.red
      self.stateCounter = 0
    if self.state != prevState:
      self.hide()
      self.show()     
  
#------------------------------------
# Основная программа
#------------------------------------
app = TApplication("Дорога и машины")
app.size = (500, 200)

canvas = TCanvas(app, bg="white")
canvas.align = "client"

#------------------------------------
# Построение объектов - дорога и машины
# + светофор
#------------------------------------
road = TRoad(430, 3)

light = TLight(220, "light", canvas)
light.show()

# Добавляем светофор на дорогу
road.addLight(light)

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
  light.timeStep()        # работа светофора по таймеру   
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


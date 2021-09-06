from turtle import *
from math import *

вп = вперед = forward
нз = назад = backward
нл = налево = left
нп = направо = right
пп = поднять_перо = penup
оп = опустить_перо = pendown
ф = форма = shape #“arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”
шт = штамп = stamp
цвет = color
зн = закрась_начало = begin_fill
зк = закрась_конец = end_fill
перо = width
переход = goto
очистить = clear
домой = home

ф('turtle')
нл(90)
def big(n):
    for i in range(n):
        вп(200)
        нп(360/n*3)


     

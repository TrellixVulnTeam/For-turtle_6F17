#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_10():
    x=0
    while not wall_is_on_the_right() and wall_is_above():#ищем первый выход вверх
        move_right() 
        x+=1
    up() if wall_is_above()==False else cell_is_filled()

    move_left(x) if x>0 else cell_is_filled()

    x=0
    while not wall_is_on_the_right() and wall_is_beneath():#ищем первый выход вниз
        move_right() 
        x+=1
    down() if wall_is_beneath()==False else cell_is_filled()
    
    while not wall_is_on_the_right():
        move_right() 

       
def up ():
    y=0
    move_up()
    fill_cell()
    while not wall_is_on_the_right():
        move_right()
        y+=1
        if not wall_is_beneath():
            fill_cell()

    move_left(y)
    move_down()

def down():
    y=0
    move_down()
    fill_cell()
    while not wall_is_on_the_right():
        move_right()
        y+=1
        if not wall_is_above():
            fill_cell()
    while wall_is_above():
        move_left()
    move_up()

if __name__ == '__main__':
    run_tasks()

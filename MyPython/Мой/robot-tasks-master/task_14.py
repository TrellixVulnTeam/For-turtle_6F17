#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_11():

    while not wall_is_on_the_right() and wall_is_above():#ищем первый выход вверх
        move_right() 

    up() if wall_is_above()==False else cell_is_filled()

    while not wall_is_on_the_right():
        move_right()

    if wall_is_beneath() and wall_is_above():
        fill_cell()
    while not wall_is_on_the_left():
        move_left()
        if wall_is_beneath() and wall_is_above():
            fill_cell()

    while not wall_is_on_the_right() and wall_is_beneath():#ищем первый выход вниз
        move_right() 

    down() if wall_is_beneath()==False else cell_is_filled()

    while not wall_is_on_the_right():
        move_right()            

       
def up ():
    move_up()
    fill_cell()
    while not wall_is_on_the_right():
        move_right()
        if not wall_is_beneath():
            fill_cell()

    while wall_is_beneath():
        move_left()
    move_down()
    
def down():
    move_down()
    fill_cell()
    while not wall_is_on_the_right():
        move_right()
        if not wall_is_above():
            fill_cell()
    while wall_is_above():
        move_left()
    move_up()

if __name__ == '__main__':
    run_tasks()

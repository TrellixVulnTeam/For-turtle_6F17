#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    fill_cell()
    while not wall_is_beneath():
        right()
        move_down()
        fill_cell()
        left()
        if not wall_is_beneath():
            move_down()
            fill_cell()            
    if wall_is_on_the_right():
        left()
    else:
        right()
        left()

        
def right():
    while not wall_is_on_the_right():
        move_right()
        fill_cell()

def left():
    while not wall_is_on_the_left():
        move_left()
        fill_cell()

if __name__ == '__main__':
    run_tasks()

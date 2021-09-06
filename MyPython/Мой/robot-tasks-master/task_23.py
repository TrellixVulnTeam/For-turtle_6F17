#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_6_6():
    y=0
    while not wall_is_on_the_right():
        move_right(1)
        y+=1
        if not wall_is_above():
            k()
    move_left(y)

def k():
    x=0
    while not wall_is_above():
        move_up()
        fill_cell()
        x+=1
    move_down(x)
    
        


if __name__ == '__main__':
    run_tasks()

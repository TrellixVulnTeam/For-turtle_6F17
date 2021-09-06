#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    n=-1
    while not wall_is_on_the_right():
        move_right()
        p(n)
        n+=1

def p(n):
    f=True
    for i in range(n):
        if not wall_is_on_the_right():
            move_right()
            f=False if wall_is_on_the_right() else True
    fill_cell() if f and not wall_is_on_the_right() else cell_is_filled()
    
if __name__ == '__main__':
    run_tasks()

#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
    k=1
    while not wall_is_beneath():
        move_down()
        k+=1
    r(k-2)
    move_down(k//2)
    move_left(k//2)
    
def r(n):
    if n<1:
        return
    for i in range(n):
        move_right()
        fill_cell()
    move_right()
    for i in range(n):
        move_up()
        fill_cell()
    move_up()
    for i in range(n):
        move_left()
        fill_cell()
    move_left()
    for i in range(n):
        move_down()
        fill_cell()

    move_right()
    r(n-2)
    
if __name__ == '__main__':
    run_tasks()

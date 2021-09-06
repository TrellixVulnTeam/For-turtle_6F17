#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_2():
    move_down(n=1)
    for i in range(5):
        pic()
        move_right(4) if i<4 else  cell_is_filled()

def pic():
    move_down()
    fill_cell()
    for i in range(2):
        move_right()
        fill_cell()
    move_down()
    move_left()
    fill_cell()
    for i in range(2):
        move_up()
        fill_cell()
    move_left()

if __name__ == '__main__':
    run_tasks()

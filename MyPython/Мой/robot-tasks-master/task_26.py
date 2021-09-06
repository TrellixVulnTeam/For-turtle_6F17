#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_2_4():
    for i in range(5):
        r()
        move_left(36)
        if i<4:
            move_down(4)


def r():
    for i in range(10):
        pic()
        move_right(4) if i<9 else  cell_is_filled()

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

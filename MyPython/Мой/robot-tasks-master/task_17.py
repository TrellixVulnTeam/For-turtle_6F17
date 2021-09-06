#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_27():
    forward()
    move_right()
    move_left(2) if not cell_is_filled() else cell_is_filled()

def forward():
    while not cell_is_filled():
        move_up()

if __name__ == '__main__':
    run_tasks()

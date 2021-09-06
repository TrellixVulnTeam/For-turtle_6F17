#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    k=0
    while not wall_is_on_the_right():
        if cell_is_filled():
            k+=1
        else:
            k=0
        if k==3:
            break
        move_right()

                


if __name__ == '__main__':
    run_tasks()

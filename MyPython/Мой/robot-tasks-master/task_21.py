#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    for i in range (0,14,2):

        for j in range (i):

            move_right()
            fill_cell()

        move_right()
        move_down()

        for j in range (i+1):
            fill_cell()
            move_left()
        move_down()
                        
    move_right(n=1)



if __name__ == '__main__':
    run_tasks()

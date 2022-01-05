#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_18():
    n = 0
    while wall_is_beneath():
        if wall_is_above() and wall_is_beneath():
            fill_cell()
        if not wall_is_above():
            n = n + koridor()
        move_right()
    mov('ax', n)


def koridor():
    move_up()
    n = 0
    z = 1
    while not wall_is_above():
        if cell_is_filled():
            n += 1
        else:
            fill_cell()
        move_up()
        z += 1
    if cell_is_filled():
        n += 1
    else:
        fill_cell()

    move_down(z)
    return n


if __name__ == '__main__':
    run_tasks()

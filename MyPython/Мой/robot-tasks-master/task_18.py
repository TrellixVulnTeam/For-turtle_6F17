#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_28():
    while not wall_is_on_the_left():
        if wall_is_above():
            move_left()
        else:
            home()

    if wall_is_beneath():
        while wall_is_above():
            move_right()
        home()

def home():
    while not wall_is_above():
        move_up()
    while not wall_is_on_the_left():
        move_left()


if __name__ == '__main__':
    run_tasks()

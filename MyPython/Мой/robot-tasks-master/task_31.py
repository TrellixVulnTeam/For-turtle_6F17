#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():
    poisk_l()

def poisk_l():
    while not wall_is_on_the_left() and wall_is_beneath():
        move_left()
    if not wall_is_beneath():
        d()
    else:
        poisk_r()

def d():
    while not wall_is_beneath():
        move_down()
    poisk_l()

def poisk_r():
    while not wall_is_on_the_right() and wall_is_beneath():
        move_right()
    if not wall_is_beneath():
        d()
    else:
        end()
def end():
    while not wall_is_on_the_left():
        move_left()

if __name__ == '__main__':
    run_tasks()

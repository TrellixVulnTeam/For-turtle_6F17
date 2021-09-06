#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
    if wall_is_above():
        b()
        ch()
    elif wall_is_beneath():
        t()
        ch()
        
def ch():
    if  wall_is_on_the_left():
        r()
    else:
        l()    
def r():
    while not wall_is_on_the_right():
        move_right()
def l():
    while not wall_is_on_the_left():
        move_left()    
def t():
    while not wall_is_above():
        move_up()
def b():
    while not wall_is_beneath():
        move_down()


if __name__ == '__main__':
    run_tasks()

#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_22():
    forward()
    left() if wall_is_on_the_right() else right()

def forward():
    while not wall_is_above():
        move_up()

def left():
    while not wall_is_on_the_left():
        move_left()

def right():
    while not wall_is_on_the_right():
        move_right()
    
       
if __name__ == '__main__':
    run_tasks()

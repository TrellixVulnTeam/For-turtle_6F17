#!/usr/bin/python3

from pyrob.api import *


@task
def task_3_3():
    if not wall_is_above():
        move_up()#если сверху стена, возвращает True, иначе — False
    elif not wall_is_beneath():
        move_down()#если снизу стена, возвращает True, иначе — False
    elif not wall_is_on_the_left():
        move_left()#если слева стена, возвращает True, иначе — False
    else:
        move_right(n=1)


if __name__ == '__main__':
    run_tasks()

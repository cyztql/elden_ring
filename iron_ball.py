#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @Time : 2022/05/14 11:43 
# @File : iron_ball.py

"""
    雷恩魔法师塔,刷铁球，一次1950卢恩
    每过五分钟自动升级
"""

__author__ = 'chenyanzhi'

import time
import pydirectinput


def move_to_tower():
    pydirectinput.press('g')
    pydirectinput.press('f')
    pydirectinput.press('e')
    pydirectinput.press('e')
    time.sleep(6)


def horse_riding():
    time.sleep(2)
    pydirectinput.keyDown('e')
    pydirectinput.press('up')
    pydirectinput.keyUp('e')


def correct_direction():
    pydirectinput.press('s')
    pydirectinput.press('q')
    pydirectinput.press('a', presses=6, interval=0.6)


def go_straight():
    pydirectinput.keyDown('w')
    pydirectinput.keyDown('space')
    time.sleep(4.2)
    pydirectinput.press('a', presses=8)
    time.sleep(1.2)
    pydirectinput.press('d', presses=4)
    time.sleep(2.4)
    pydirectinput.keyUp('space')


def turn_right():
    pydirectinput.keyDown('d')
    time.sleep(2.8)
    pydirectinput.keyUp('d')
    pydirectinput.press('f')
    pydirectinput.press('f')
    time.sleep(0.5)
    pydirectinput.keyUp('w')


def back_again():
    time.sleep(5)
    pydirectinput.press('g')
    pydirectinput.press('f')
    pydirectinput.press('e')
    pydirectinput.press('e')


def strength_upgrade():
    pydirectinput.press('down')
    pydirectinput.press('down')
    pydirectinput.press('down')


def intelligence_upgrade():
    pydirectinput.press('down')
    pydirectinput.press('down')
    pydirectinput.press('down')
    pydirectinput.press('down')
    pydirectinput.press('down')


def upgrade():
    print("启动自动升级")
    back_again()
    time.sleep(8)
    pydirectinput.press('w')
    pydirectinput.press('e')
    time.sleep(3)
    pydirectinput.press('down')
    pydirectinput.press('e')
    time.sleep(3)
    strength_upgrade()
    pydirectinput.press('right')
    pydirectinput.press('right')
    pydirectinput.press('e')
    time.sleep(2)
    pydirectinput.press('left')
    pydirectinput.press('e')
    time.sleep(2)
    pydirectinput.press('q')
    time.sleep(2)
    pydirectinput.press('q')


def main():
    time.sleep(3)
    start = time.time()
    while True:
        back_again()
        move_to_tower()
        horse_riding()
        correct_direction()
        go_straight()
        turn_right()
        end = time.time()
        total_time = int(end - start)
        print(f"total time cost: {total_time}")
        if total_time > 300:
            upgrade()
            start = time.time()


if __name__ == '__main__':
    main()

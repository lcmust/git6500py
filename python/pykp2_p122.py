#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
PYTHON核心编译第2版p122P98习题5.5
"""

import os
import sys
result = {'25':0, '10':0, '5':0, '1':0}
money = int(raw_input("input a number:"))
def fun():
    global result
    global money
    if money == 0:
        return
    if (money >= 25):
        result['25'] += 1
        money -= 25
        fun()
    elif (money >= 10):
        result['10'] += 1
        money -= 10
        fun()
    elif (money >= 5):
        result['5'] += 1
        money -= 5
        fun()
    elif (money >= 1):
        result['1'] += 1
        money -= 1
        fun()

if __name__ == "__main__":
    print result
    fun()
    print result
    print "over"

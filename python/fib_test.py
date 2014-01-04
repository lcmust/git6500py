#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import datetime

print datetime.datetime.now()
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

class Abc():
    msg = "Hello Abc-class"
    def print_abc(self):
        print self.msg


class Abd():
    msg = "hello Abd-class"
    def print_abd(self):
        print self.msg

print datetime.datetime.now()

if __name__ == "__main__":
    number = raw_input("Input a number(0-30):")
    result = fib(int(number))
    if result:
        print("the fib(40) result = %d\n")  % result;
    for i in range(len(sys.argv)):
        print sys.argv[i]

    print datetime.datetime.now()

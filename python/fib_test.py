#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

if __name__ == "__main__":
    number = raw_input("Input a number(0-30):")
    result = fib(int(number))
    if result:
        print("the fib(40) result = %d\n")  % result;
    for i in range(len(sys.argv)):
        print sys.argv[i]

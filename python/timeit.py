#!/usr/bin/python
# -*- coding: utf-8 -*-
import time

def timeit(func):
    def wrapper():
        start = time.clock()
        func()
        end = time.clock()
        print "used time:", end - start, "s"
    return wrapper

@timeit
def foo():
    print "in foo()"
    i1 = 0
    while(1):
        i1 = i1 + 1
        if i1 > 10000000:
            break

if __name__ == "__main__":
    foo()

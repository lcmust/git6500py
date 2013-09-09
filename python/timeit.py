#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import os
import sys

def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.clock()
        func(*args, **kwargs)
        end = time.clock()
        print type(end)
        print "used time:%f seconds" % (end - start)
    return wrapper

@timeit
def foo(argu=2000):
    print "in foo()"
    i1 = 0
    while(1):
        i1 = i1 + 1
        if i1 > argu:
            break

if __name__ == "__main__":
    if len(sys.argv) > 1:
        foo(int(sys.argv[1]))
    else:
        foo()

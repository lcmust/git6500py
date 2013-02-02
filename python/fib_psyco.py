#!/usr/bin/env python
# -*- coding: utf-8 -*-
import psyco
psyco.full()
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

if __name__ == "__main__":
    fib(40)

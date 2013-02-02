#!/usr/bin/env python
# -*- coding: utf-8 -*-
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

if __name__ == "__main__":
	result = fib(40)
	if result:
		print("the fib(40) result = %d\n")  % result;


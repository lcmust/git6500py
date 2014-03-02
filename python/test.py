#! /usr/bin/env python
#coding=utf-8
import os
gettest = lambda s: s
PROJECT_PATH = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
print gettest
print PROJECT_PATH
print os.path.split(os.path.abspath(os.path.dirname(__file__)))

class Message:
    def __init__(self, msg):
        self.msg = msg

class Message2:
    def __init__(self, msg):
        self.msg = msg

    def __repr__(self):
        return "Message: %s" % self.msg

def foo(bar):
    return bar + 1

print foo(2) == 3

def call_foo_with_arg(foo, arg):
    return foo(arg)

def parent(num):
    def first_child():
        return "Print from the first child() function."

    def second_child():
        return "Print from the second child() function."

    try:
        assert num == 10
        return first_child
    except AssertionError:
        return second_child
    

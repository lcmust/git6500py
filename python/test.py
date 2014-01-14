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

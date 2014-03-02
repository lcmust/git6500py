#!/usr/bin/env python
#coding=utf-8
import socket
solist = [x for x in dir(socket) if x.startswith('SO_')]
solist.sort()
line_no = 1
for x in solist:
    print line_no, x
    line_no += 1

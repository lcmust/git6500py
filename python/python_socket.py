#!/usr/bin/python
#-*- coding:utf-8 -*-
#filename:python_socket.py

import os
import sys
import time
import socket

s = socket.socket()
try:
    if sys.argv[1]:
        tmp = sys.argv[1].split(':')
        host = tmp[0]
        port = int(tmp[1])
except:
    host = socket.gethostname()
    port = 12345
    print("newer, host(%s), port(%d)" % ( host, port))

s.bind((host, port))
s.listen(5)
while True:
    c = s.accept()
    #print type(c) >>> tuple
    print( 'Got connection from', c[1], time.ctime() )
    c[0].send('Thank you for connecting\n')
    c[0].close()


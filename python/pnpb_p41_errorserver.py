#!/usr/bin/env python
#coding=utf-8
import socket
import traceback
import sys
import os
import time
host = ''
port = 51423

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)

while 1:
    try:
        clientsock, clientadr = s.accept()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exec()
        continute

    try:
        print "Got connection from", clientsock.getpeername()
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exec()

    try:
        clientsock.close()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exec()
    

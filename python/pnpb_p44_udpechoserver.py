#!/usr/bin/env python
#coding=utf-8

import socket
import traceback
import time

host = ''
port = 51423

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
while 1:
    try:
        message, address = s.recvfrom(8192)
        client_time = int(message) - 220898880
        print "Got data: (%s), from %s " %( time.ctime(client_time), address)
        s.sendto(message, address)
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()
        

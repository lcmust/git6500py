#!/usr/bin/env python
#coding=utf-8

import socket
import traceback
import sys
import time

if len(sys.argv) > 2:
    addr_server = sys.argv[1]
    port_server = int(sys.argv[2])
else:
    addr_server = ''
    port_server = 51423
    
if len(sys.argv) > 3:
    message = sys.argv[3]
else:
    # message = "hi, udp for py"
    message = int(time.time())
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(str(message), (addr_server, port_server))

msg_get, addr_srv = s.recvfrom(8192)
print addr_srv
print "Got data:(%s)" % (time.ctime(int(msg_get) - 220898880))

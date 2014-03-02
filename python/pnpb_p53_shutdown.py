#!/usr/bin/env python
#coding=utf-8
import socket
import sys
import time
print len(sys.argv)
if len(sys.argv) == 3:
    print sys.argv[0], sys.argv[1], sys.argv[2]
if not True:
    host = sys.argv[1]
    textport = sys.argv[2]
    filename = sys.argv[3]
else:
    host = "192.168.192.1"
    textport = "80"
    filename = "/Front_Page.asp"

print "Creating socket..."
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, e:
    print "a error when socket.socket: %s" % e
    sys.exit(1)
print "Done!"

print "connecting to remote host..."
try:
    s.connect((host, int(textport)))
except socket.error, e:
    print "a error when connect: %s" % e
    sys.exit(1)
print "Done!"

fd = s.makefile('rw', 0)

print "sleeping..."
time.sleep(4)
print "continuing!"

print "getting infomation..."
try:
    fd.write("GET %s HTTP/1.0 \r\n\r\n" % filename)
except socket.error, e:
    print "a error when sendall: %s" % e
    sys.exit(1)
print "Done!"

try:
    fd.flush()
except socket.error, e:
    print "a error when fd.flush: %s" % e
    sys.exit(1)

try:
    s.shutdown(1)
    s.close()
except socket.error, e:
    print "a error when shutdown: %s" % e
    sys.exit(1)
    
while 1:
    try:
        buf = fd.read(2048)
    except socket.error, e:
        print "a error when fd.read: %s" % e
        sys.exit(1)
    if not len(buf):
        break
    sys.stdout.write(buf)

#!/usr/bin/env python
#coding=utf-8
import socket
import sys

#host = "192.168.192.1"
#textport = "80"
#filename = "/Front_Page.asp"
if len(sys.argv) == 3:
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

print "getting infomation..."
try:
    s.sendall("GET %s HTTP/1.0\r\n\r\n" % filename)
except socket.error, e:
    print "a error when sendall: %s" % e
    sys.exit(1)
print "Done!"
while 1:
    try:
        buf = s.recv(2048)
    except socket.error, e:
        print "a error when recv: %s" % e
        sys.exit(1)
    if not len(buf):
        break
    sys.stdout.write(buf)

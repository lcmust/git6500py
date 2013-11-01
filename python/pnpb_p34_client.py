#!/usr/bin/python
# Simple Gopher Client - chapter 1
import socket, sys

port = 70
host = sys.argv[1]
filename = sys.argv[2]

a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    a.connect((host, port))
except socket.gaierror, e:
    print "Error connecting to server: %s" % e
    sys.exit(1)

fd = a.makefile("rw", 0)
fd.write(filename + "\r\n")
"""
a.sendall(filename + "\r\n")

while 1:
    buf = a.recv(2048)
    if not len(buf):
        break
    sys.stdout.write(buf)
"""
for line in fd.readlines():
    sys.stdout.write(line)

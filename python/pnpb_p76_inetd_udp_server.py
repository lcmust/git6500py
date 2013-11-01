#!/usr/bin/python
import socket, time, sys

s = socket.fromfd(sys.stdin.fileno(), socket.AF_INET, socket.SOCK_DGRAM)
message, client_addr = s.recvfrom(8192)
s.connect(client_addr)
for i in range(10):
    s.send("Reply %d: %d" % (i + 1, message))
    time.sleep(2)
s.send("Ok, I'm done sending replies.\n")

#!/usr/bin/python
import socket
import sys
host = ""
#port = 51423
if (len(sys.argv) > 1):
    try:
        port = int(sys.argv[1])
    except ValueError:
        try:
            port = socket.getservbyname(sys.argv[1], 'tcp')
        except socket.error, e:
            print "Couldn't find your port: %s" % e
            sys.exit(1)
else:
    port = 51234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)

print "Server is running on port %d, press Ctrl+C to terminate." % port
while 1:
    clientsock, clientaddr = s.accept()
    print "Server is:", clientsock.getsockname()
    print "New connection from:", clientsock.getpeername()
    # print "clientaddr:%s" % str(clientaddr) 
    clientfile = clientsock.makefile("rw", 0)
    clientfile.write("Welcome, " + str(clientaddr) + "\n")
    clientfile.write("PLease enter a string:")
    line = clientfile.readline().strip()
    clientfile.write("You entered %d characterts.\n" % len(line))
    clientfile.close()
    clientsock.close()
    print str(clientaddr) + "connecting is closed."

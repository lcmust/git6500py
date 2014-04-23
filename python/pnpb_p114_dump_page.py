#!/usr/bin/env python
#coding=utf-8

import sys, urllib2

req = urllib2.Request(sys.argv[1])
fd = urllib2.urlopen(req)
print "Retrieved", fd.geturl()
info = fd.info()
for key, value in info.items():
    print "%s = %s" %(key, value)
    
while 1:
    data = fd.read(1024)
    if not len(data):
        break
    sys.stdout.write(data)

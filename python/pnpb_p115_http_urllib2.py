#!/usr/bin/env python 
#coding=utf-8
import sys, urllib2
if (len(sys.argv) > 1):
    req = urllib2.Request(sys.argv[1])
else:
    req = urllib2.Request("http://192.168.0.1/")
fd = urllib2.urlopen(req)
print "Retieved", fd.geturl()
info = fd.info()
for key, value in info.items():
    print "%s = %s" %(key, value)

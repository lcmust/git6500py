#!/usr/bin/env python
#coding=utf-8

import sys, urllib2

if len(sys.argv) > 2:
    req = urllib2.Request(sys.argv[1])
else:
    req = urllib2.Request('http://localhost')
try:
    fd = urllib2.urlopen(req)
except urllib2.URLError, e:
    print "Error retrieving data:", e
    sys.exit(1)

print "Retrieved", fd.geturl()
info = fd.info()
for key, value in info.items():
    print "%s = %s" %(key, value)

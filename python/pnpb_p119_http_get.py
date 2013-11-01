#!/usr/bin/env python
#coding=utf-8

import sys, urllib2, urllib

if len(sys.argv) > 1:
    zipcode = sys.argv[1]
else:
    zipcode = 10001

def addGetData(url, data):
    return url + "?" + urllib.urlencode(data)

url = "http://www.wunderground.com/cgi-bin/findweather/getForecast"
url2 = addGetData(url, [('query', zipcode)])
print "Using URL:", url2
req = urllib2.Request(url2)
fd = urllib2.urlopen(req)

while 1:
    data = fd.read(1024)
    if not len(data):
        break
    sys.stdout.write(data)

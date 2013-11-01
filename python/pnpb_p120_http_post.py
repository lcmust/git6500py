#!/usr/bin/env python
#coding=utf-8

import sys, urllib2, urllib

if len(sys.argv) > 1:
    zipcode = sys.argv[1]
else:
    zipcode = 10001

url = "http://www.wunderground.com/cgi-bin/findweather/getForecast"
data = urllib.urlencode([('query', zipcode)])
req = urllib2.Request(url)
fd = urllib2.urlopen(req, data)

while 1:
    data = fd.read(1024)
    if not len(data):
        break
    sys.stdout.write(data)

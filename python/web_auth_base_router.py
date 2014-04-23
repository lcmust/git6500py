#!/usr/bin/python
#coding=utf8
#filename=web_auth_base_router.py
'''
'''
import urllib
import urllib2
import base64
import time
url = "http://192.168.1.1/"
url2 = "http://192.168.1.1/index.asp"
user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
username = 'admin'
password = 'admin'
headers = {'User-Agent': user_agent,
           'Authorization': "Basic " +
           base64.b64encode(username + ":" + password)}
#print headers
req = urllib2.Request(url = url, headers = headers)
try:
    response = urllib2.urlopen(req)
except (urllib2.HTTPError, urllib2.URLError),e:
    print e

page = response.read()
if response.getcode() == 200:
    print time.asctime(),"Access<" + url + "> is OK"

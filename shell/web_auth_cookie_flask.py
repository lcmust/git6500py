#!/usr/bin/python
#coding=utf8
#filename:web_auth_cookie_flask.py
'''
'''
import urllib
import urllib2
import cookielib
import time

url = "http://127.0.0.1:5000"
url_login = url + "/login"

user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
headers = {'User-Agent':user_agent}
values = {'username':'admin', 'password':'admin', }
datas = urllib.urlencode(values)

#print values['username'],values['password']
#print headers
#req = urllib2.Request(url, data, headers)
cookiejar = cookielib.MozillaCookieJar('/tmp/cookie_scxh1.txt')
cookieproc = urllib2.HTTPCookieProcessor(cookiejar)
opener = urllib2.build_opener(cookieproc)
req = urllib2.Request(url=url_login, data=datas, headers=headers)

try:
    response = opener.open(req)
except (urllib2.HTTPError, urllib2.URLError),e:
    print e
page = response.read()
if response.getcode() == 200:
    cookiejar.save(ignore_discard=True, ignore_expires=True)
    print time.asctime(),"Access<" + url_login + "> is OK"


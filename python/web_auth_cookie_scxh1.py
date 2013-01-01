#!/usr/bin/python
#coding=utf8
#filename:web_auth_cookie_scxh1.py
'''
'''
import urllib
import urllib2
import cookielib
import time

url = "http://www.scxhedu.com:86"
url_login = url + "/育才小学/UserLogin.asp"
url_login_uni = unicode(url_login, 'utf-8')
url_login_gb2312 = url_login_uni.encode('gb2312')

user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
headers = {'User-Agent':user_agent}
values = {'UserName':'admin', 'Password':'admin', }
datas = urllib.urlencode(values)

#print values['username'],values['password']
#print headers
#req = urllib2.Request(url, data, headers)
cookiejar = cookielib.MozillaCookieJar('/tmp/cookie_scxh1.txt')
cookieproc = urllib2.HTTPCookieProcessor(cookiejar)
opener = urllib2.build_opener(cookieproc)
req = urllib2.Request(url=url_login_gb2312, data=datas, headers=headers)

'''
try:
    response = opener.open(req)
except (urllib2.HTTPError, urllib2.URLError),e:
    print e
page = response.read()
if response.getcode() == 200:
    cookiejar.save(ignore_discard=True, ignore_expires=True)
    print time.asctime(),"Access<" + url_login + "> is OK"
'''

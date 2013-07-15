#!/usr/bin/python
#coding=utf8
#filename=web_auth_base_router.py
'''
'''
import urllib
import urllib2
import base64
import time
url = "http://192.168.192.168:8844/"
#url = "http://192.168.192.168/index.asp"
user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
#username = 'admin'
username = "love"
password = 'a112B112'
#headers = {'User-Agent':user_agent}
#headers['Authorization'] = base64.b64encode(username+":"+password)
headers = {'User-Agent':user_agent, \
           'Authorization': \
           "Basic "+base64.b64encode(username+":"+password)}
#print values['username'],values['password']
#print headers
#req = urllib2.Request(url, data, headers)
req = urllib2.Request(url=url, headers=headers)
print password," ", username
""" ###print headers
{'Authorization': 'Basic bG92ZTphMTEyQjExMg==', 'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
"""
try:
    response = urllib2.urlopen(req)
except (urllib2.HTTPError, urllib2.URLError),e:
    print e
    exit(0)
page = response.read()
if response.getcode() == 200:
    print time.asctime(),"Access<" + url + "> is OK"
    print page

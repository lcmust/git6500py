#!/usr/bin/env python
#coding=utf-8

from HTMLParser import HTMLParser
import sys

class TitleParser(HTMLParser):
    def __init__(self):
        self.title = ''
        self.readingtitle = 0
        HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
        if tag == 'title':
            self.readingtitle = 1

    def handle_data(self, data):
        if self.readingtitle:
            self.title += data

    def handle_endtag(self, tag):
        if tag == 'title':
            self.readingtitle = 0

    def gettitle(self):
        return self.title

class TableParser(HTMLParser):
    def __init__(self):
        self.table = ''
        self.readingtitle = 0
        HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
        if tag == 'table':
            self.readingtitle = 1

    def handle_data(self, data):
        if self.readingtitle:
            self.table += data

    def handle_endtag(self, tag):
        if tag == 'table':
            self.readingtitle = 0

    def gettable(self):
        return self.table

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

def web_data(url="http://192.168.192.1/Front_Page.asp"):
    import urllib2
    resp = urllib2.Request(url)
    resp1 = urllib2.urlopen(resp)
    resp2 = resp1.read()
    return resp2

def get_resu(data, target="title"):
    if not data:
        return
    target = TargetParser(target=target)
    target.feed(data)
    resu = target.getresu()
    return resu

test_data = """<!DOCTYPE html>
<html>
    <head>
        <title>All Contacts.</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            .container {
              padding: 50px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>All contacts</h1>
            <table border="1" cellpadding="5">
                <tr>
                    <th>First Name</th>
                    <th>Last name</th>
                    <th>Address</th>
                    <th>City</th>
                    <th>State</th>
                    <th>Country</th>
                    <th>Number</th>
                    <th>Email</th>
                </tr>

                <tr>
                    <td>liu </td>
                    <td>cheng</td>
                    <td>28 longjin road</td>
                    <td>chengdu</td>
                    <td>61000</td>
                    <td>china</td>
                    <td>123456789</td>
                    <td>lcc@test.com</td>
                </tr>

                <tr>
                    <td>五 </td>
                    <td>名</td>
                    <td>23 longjin road</td>
                    <td>beijin</td>
                    <td>100000</td>
                    <td>china</td>
                    <td>987654321</td>
                    <td>wumiin@test.com</td>
                </tr>

                <tr>
                    <td>firstname </td>
                    <td>lastname</td>
                    <td>first3 last3 road</td>
                    <td>chengdu</td>
                    <td>sichuang</td>
                    <td>china</td>
                    <td>9090950</td>
                    <td>474944723@qq.com</td>
                </tr>

            </table>
            <br />
            <a href="../">Return Home</a>
        </div>
    </body>
</html>
"""


if __name__ == '__main__':
    title = get_resu(test_data)
    table = get_resu(test_data, target="table")
    print title
    print table

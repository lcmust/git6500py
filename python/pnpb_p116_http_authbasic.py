#!/usr/bin/env python
#coding=utf-8

import sys, urllib2, getpass

class TerminalPassword(urllib2.HTTPPasswordMgr):
    def find_user_password(self, realm, authuri):
        retval = urllib2.HTTPPasswordMgr.find_user_password(self, realm, authuri)

        if retval[0] == None and retval[1] == None:
            sys.stdout.write("Login required for %s at %s\n" % (realm, authuri));
            sys.stdout.write("Username:");
            username = sys.stdin.readline().rstrip()
            password = getpass.getpass().rstrip()
            return (username, password)
        else:
            return retval


def test(url):
    req = urllib2.Request(url)
    opener = urllib2.build_opener(urllib2.HTTPBasicAuthHandler(TerminalPassword()))
    fd = opener.open(req)
    print "Retrieved", fd.geturl()
    info = fd.info()
    for key, value in info.items():
        print "%s = %s" %(key, value)

if __name__ == "__main__":
    print "begin..."
    if (len(sys.argv) > 1):
        url_open = sys.argv[1]
    else:
        url_open = "http://192.168.192.1/index.asp"
    if url_open:
        test(url_open)

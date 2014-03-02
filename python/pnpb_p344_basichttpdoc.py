#!/usr/bin/env python
#coding=utf-8
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import time

starttime = time.time()

class RequestHandler(BaseHTTPRequestHandler):
    """definition of the request handler."""
    def _writeheaders(self, doc):
        """Write the HTTP headers for the document, If there's no document,
        sned a 404 error code; otherwise, send a 200 success code."""
        if doc is None:
            self.send_response(404)
        else:
            self.send_response(200)

        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def _getdoc(self, filename):
        """Handle a request for a document, returning one of two
         different pages as appropriate."""
        global starttime
        if filename == "/":
            return """<html><head><title>Sample Page</title></head>
            <body>THis is a sample page. You can also look at the
            <a href="stats.html">server statistics</a></body></html>"""
        elif filename == "/stats.html":
            return """<html><head><title>Statistics</title></head>
            <body>This server has been running for %d seconds.</body>
            </html>""" % int(time.time() - starttime)
        elif filename == "/default.html":
            return """<html><head><title>Hi guys.</title></head>
            <body>Welcome, everybody!</body>
            </html>"""
        else:
            return None

    def do_HEAD(self):
        """Handle a request for headers only"""
        doc = self._getdoc(self.path)
        self._writeheaders(doc)

    def do_GET(self):
        """Handle a request for headers and body"""
        doc = self._getdoc(self.path)
        self._writeheaders(doc)
        print "debug(self.path => )", self.path
        # print the current URL's path
        
        if doc is None:
            self.wfile.write("""<html><head><title>Not Found</title></head>
            <body>The requested document '%s' was not found.</body>
            </html>""" % self.path)
        else:
            self.wfile.write(doc)

serveraddr = ('', 8765)
srvr = HTTPServer(serveraddr, RequestHandler)
srvr.serve_forever()

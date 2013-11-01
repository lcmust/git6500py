#!/usr/bin/env python

import sys
import tftpy
from os import unlink
from os.path import basename, isdir
from getopt import GetoptError, getopt as GetOpt

DEFAULT_FILE = '/dev/null'
DEFAULT_ACTION = 'get'
DEFAULT_PORT = 69
DEFAULT_TIMEOUT = 5

def usage():
	print ""
	print "Usage: tfcp [OPTIONS] [<host:file> <file>]"
	print "                      [<file> <host:file>]"
	print ""
	print "Options:"
	print "\t-P, --port=<port>              TFTP server port [%d]" % DEFAULT_PORT
	print "\t-t, --timeout=<seconds>        Connection timeout period [%d]" % DEFAULT_TIMEOUT
	print "\t-q, --quiet                    Do not display warnings"
	print ""
	print "Examples:"
	print "\t$ tfcp 127.0.0.1:/foo /tmp/bar"
	print "\t$ tfcp /tmp/bar 127.0.0.1:/foo"
	print ""

	sys.exit(1)

def main():

	e = None
	host = None
	quiet = False
	local_file = None
	remote_file = None
	port = DEFAULT_PORT
	timeout = DEFAULT_TIMEOUT
	action = DEFAULT_ACTION
	
	if len(sys.argv) < 3:
		usage()

	try:
		opts, args = GetOpt(sys.argv[1:], 'P:t:hq', ['port=', 'timeout=', '--help', '--quiet'])
	except GetoptError, e:
		print "Error: %s" % str(e)
		usage()

	for opt, arg in opts:
		if opt in ('-h', '--help'):
			usage()
			remote_file = arg
		elif opt in ('-P', '--port'):
			port = int(arg)
		elif opt in ('-t', '--timeout'):
			timeout = int(arg)
		elif opt in ('-q', '--quiet'):
			quiet = True

	src = sys.argv[-2]
	dst = sys.argv[-1]

	if ':' in src:
		action = 'get'
		local_file = dst
		host, remote_file = src.split(':', 1)
	elif ':' in dst:
		action = 'put'
		local_file = src
		host, remote_file = dst.split(':', 1)
	else:
		usage()

	
	if host is None:
		print "Error: please specify a remote host"
		usage()
	elif action == 'get' and remote_file is None:
		remote_file = DEFAULT_FILE
		if not quiet:
			print "Warning: no remote file specified, requesting '%s'" % remote_file
	elif action == 'put' and local_file is None: 
		local_file = DEFAULT_FILE
		if not quiet:
			print "Warning: no local file specified, uploading '%s'" % local_file

	if action == 'get' and isdir(local_file):
		local_file = "%s/%s" % (local_file, basename(remote_file))
	elif action == 'put' and remote_file is None:
		remote_file = basename(local_file)

	tftp = tftpy.TftpClient(host, port)
	
	try:
		if action == 'put':
			tftp.upload(remote_file, local_file, timeout=timeout)
		elif action == 'get':
			tftp.download(remote_file, local_file, timeout=timeout)
	except tftpy.TftpException, e:
		print "%s failed: %s" % (action, str(e))
	except TypeError, e:
		print "%s failed: timeout" % action
	except Exception, e:
		print "%s failed: %s" % (action, str(e))

	if e is not None and action == 'get':
		unlink(local_file)

if __name__ == "__main__":
	main()

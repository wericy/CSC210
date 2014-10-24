#!/usr/bin/python

import cgi, Cookie

import cgitb
cgitb.enable()

cook = Cookie.SimpleCookie()
cook['session_id'] = ''
cook['session_id']['max-age'] = 1
print "Content-type: text/html"
print cook
print 
print "You have been logged out"
print "<a href='../index.html'>Go to Index</a>"
	
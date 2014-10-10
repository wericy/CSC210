#!/usr/bin/python


# Author: Philip Guo - CSC 210

import cgi
import datetime

# to facilitate debugging
import cgitb
cgitb.enable()

t = str(datetime.datetime.now())

import os
cookie_string = os.environ.get('HTTP_COOKIE')

import Cookie

if cookie_string:
    c = Cookie.SimpleCookie(cookie_string)

    print "Content-type: text/html"
    print # don't forget newline

    print "<html>"
    print "<body>"
    print "<h1>Hello I already have your cookie!</h1>"
    print "<h2>Your cookie's saved time is: " + c['current_time'].value + "</h2>"
    print "</body>"
    print "</html>"
else:
    c = Cookie.SimpleCookie()
    c['app_name'] = 'my_cool_app'
    c['current_time'] = t

    print "Content-type: text/html"
    print c
    print # don't forget newline

    print "<html>"
    print "<body>"
    print "<h1>Hello I'm sending a cookie to you!</h1>"
    print "<h2>The time is: " + t + "</h2>"
    print "</body>"
    print "</html>"
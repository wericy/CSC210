#!/usr/bin/python


# Philip Guo - CSC 210 modiefied by Ye Wang


import cgi
import datetime
import socket

# to facilitate debugging
import cgitb
cgitb.enable()

import sqlite3

form = cgi.FieldStorage()

print "Content-type: text/html"
# don't forget the extra newline!
print

print "<html>"
print "<head><title>My webpage</title></head>"
print "<body>"
print "<h1>Hello world!!!!!!!!</h1>"
print "<h2>Your IP address is: " + str(socket.gethostbyname(socket.gethostname())) + "</h2>"
print "<h2>The time is: " + str(datetime.datetime.now()) + "</h2>"
print "<h2>Your name is: " + form['my_name'].value + "</h2>"
print "<h2>Your age is: " + form['my_age'].value + "</h2>"
print "</body>"
print "</html>"

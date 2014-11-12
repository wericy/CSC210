#!/usr/bin/python

import cgi, Cookie, os, sqlite3
import cgitb
cgitb.enable()

conn = sqlite3.connect('person.db')
c = conn.cursor()

cookie_string = os.environ.get('HTTP_COOKIE')
if cookie_string:
	my_cookie = Cookie.SimpleCookie(cookie_string)
	saved_session_id = my_cookie['session_id'].value
	c.execute('select * from users where sessionID=?', (saved_session_id,))
	all_results = c.fetchall()
	if len(all_results) > 0:
		saved_name = all_results[0][0]
		print "Content-type: application/json"
		print # don't forget newline
		print '{"name": "%s", "login":1}' %(saved_name)
	else:
		print "Content-type: application/json"
		print # don't forget newline
		print '{"name": "invalid", "login":0}' 
   
else:
	print "Content-type: application/json"
	print # don't forget newline
	print '{"name": "invalid", "login":0}' 
	
#print "Content-type: text/plain"
#print "Content-type: application/json" 
#print 
#print "yay"

#import datetime
#print str(datetime.datetime.now())

#print '{"name": "Alice", "age": 3.14159}'

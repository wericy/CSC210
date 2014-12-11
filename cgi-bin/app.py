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
		print "Content-type: text/html"
		print 
		print "<html>"
		print "<body>"
		print "<h1>You already logged in as " + saved_name + ", please log out first</h1>"
		print "<a href='../index.html'>Go to Index</a>"
		print "</body>"
		print "</html>"
    else:
		print "Content-type: text/html"
		print 
		print "<html>"
		print "<body>"
		print "<h1>Error, wrong session_id</h1>"
		print "<a href='../index.html'>Go to Index</a>"
		print "</body>"
		print "</html>"
else:
	form = cgi.FieldStorage()
	my_name = form['my_name'].value
	my_pass = form['my_pass'].value
	c.execute('select * from users where name=? and pass=?;', (my_name,my_pass,))
	all_results = c.fetchall()
	if len(all_results) > 0:
		import uuid
		import datetime
		session_id = str(uuid.uuid4())
		c.execute('update users set sessionID=? where name=?',
				(session_id, my_name))
		conn.commit()
		
		cook = Cookie.SimpleCookie()
		cook['session_id'] = session_id
		cook['session_id']['max-age'] = 604800
		#expires = datetime.datetime.now() + datetime.timedelta(hours=1)
		#cook['session_id']['expires'] = expires.strftime('%a, %d %b %Y %H:%M:%S')
		
		print "Content-type: text/html"
		print cook
		print 
		print "<html>"
		print "<body>"
		print "<h1>Hello, " + my_name +". You're now logged in.</h1>"
		print "<a href='../index.html'>Go to Index</a>"
		print "</body>"
		print "</html>"
	else:
		print "Content-type: text/html"
		print 
		print "<html>"
		print "<body>"
		print "<h1>Unable to login,Wrong name or password</h1>"
		print "<a href='../index.html'>Go to Index</a>"
		print "</body>"
		print "</html>"

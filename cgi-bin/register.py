#!/usr/bin/python
import cgi, Cookie, os, sqlite3
import cgitb
cgitb.enable()

conn = sqlite3.connect('person.db')
c = conn.cursor()

form = cgi.FieldStorage()
my_name = form['my_namer'].value
my_pass = form['my_passer'].value
c.execute('select * from users where name=?;', (my_name,))
all_results = c.fetchall()
if len(all_results)>0:
	print "Content-type: text/html"
	print 
	print "<html>"
	print "<body>"
	print "<h1>Sorry,this name has already been taken</h1>"
	print "<a href='../index.html'>Go to Index</a>"
	print "</body>"
	print "</html>"
else:
	c.execute("INSERT INTO users VALUES (?,?,null);", (my_name,my_pass,))
	conn.commit()
	print "Content-type: text/html"
	print 
	print "<html>"
	print "<body>"
	print "<h1>Account created</h1>"
	print "<a href='../index.html'>Go to Index</a>"
	print "</body>"
	print "</html>"
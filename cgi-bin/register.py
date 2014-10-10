#!/usr/bin/python
import cgi, Cookie, os, sqlite3
import cgitb
cgitb.enable()

conn = sqlite3.connect('person.db')
c = conn.cursor()

form = cgi.FieldStorage()
my_name = form['my_namer'].value
c.execute('select * from users where name=?;', (my_name,))
all_results = c.fetchall()
if len(all_results)>0:
	print "Content-type: text/html"
	print # don't forget newline
	print "<html>"
	print "<body>"
	print "<h1>Sorry,this name has already been taken</h1>"
	print "</body>"
	print "</html>"
else:
	c.execute("INSERT INTO users VALUES (?,null);", (my_name,))
	conn.commit()
	print "Content-type: text/html"
	print # don't forget newline
	print "<html>"
	print "<body>"
	print "<h1>Account created</h1>"
	print "</body>"
	print "</html>"
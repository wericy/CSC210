#!/usr/bin/python
import cgi, Cookie, os, sqlite3
import cgitb
cgitb.enable()

conn = sqlite3.connect('person.db')
c = conn.cursor()

form = cgi.FieldStorage()
message=form.getvalue("msg", "error")
name=form.getvalue("name", "error")
c.execute('INSERT INTO chatinfo(name,say) VALUES (?,?);', (name,message))
conn.commit()

print "Content-type: text/plain"
print # don't forget newline
print "%s" %(message)
print "%s" %(name)


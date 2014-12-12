#!/usr/bin/python

import cgi, sqlite3, json
import cgitb
cgitb.enable()

form = cgi.FieldStorage()
did = form.getvalue("id", "error")
conn = sqlite3.connect('person.db')
c = conn.cursor()
c.execute('delete from chatinfo where rowid=?;', (did,))
conn.commit()
print "Content-type: text/plain"
print # don't forget newline
print did
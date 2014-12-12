#!/usr/bin/python

import cgi, sqlite3, json
import cgitb
cgitb.enable()

form = cgi.FieldStorage()
username = form.getvalue("nameex", "error")


#conn = sqlite3.connect('person.db')
#cursor = conn.cursor()
#cursor.execute("select * from chatinfo where name = ?;", (username,))
#cursor.execute("select * from chatinfo where name = 'Ye';")
#print cursor.fetchone()
#chats = []
#for row in cursor.execute("select * from chatinfo where name = 'Ye';"):
#	print row
#for row in cursor.execute('select * from chatinfo where name = ?',(username,)):
# print row
  #chats.append(row)
#chatssJSON = json.dumps(cursor.fetchone())
#
#print "Content-type: application/json"
#print 
#for row in cursor.execute("select * from chatinfo where name = ?;", (username,)):
#	print row
#print chatssJSON


DB = "person.db"

def get_all_users( json_str = False ):
    conn = sqlite3.connect( DB )
    conn.row_factory = sqlite3.Row 
    db = conn.cursor()

    rows = db.execute("select rowid,name,say,datetime(CURRENT_TIMESTAMP,'localtime') from chatinfo where name = ?;", (username,)).fetchall()

    conn.commit()
    conn.close()

    if json_str:
        return json.dumps( [dict(ix) for ix in rows] ) 

    return rows
print "Content-type: application/json"
print 
print get_all_users(json_str = True )
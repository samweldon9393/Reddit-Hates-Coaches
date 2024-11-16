import sqlite3
#open the database
conn = sqlite3.connect('comments.db')
cursor = conn.cursor()

#removing misatributed comments
blake = 'blake'
ag = 'Adrian Griffin'
#karl = "karl"
#mm = "Michael Malone"
#jv = 'Jacque Vaughn'
#jj = 'jacquez'


#pull all of the JV rows
cursor.execute("SELECT id, comment FROM coaches WHERE coach = ?", (ag,))
rows = cursor.fetchall()

#look for the substring, delete those rows
for row in rows:
    row_id, comment = row
    if blake in comment.lower():
        print(comment)
        cursor.execute("DELETE FROM coaches WHERE id = ?", (row_id,))

conn.commit()
conn.close()

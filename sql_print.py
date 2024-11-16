import sqlite3
from pprint import pprint

conn = sqlite3.connect('coaches.db')
cursor = conn.cursor()

# Fetch all rows from the table
cursor.execute('SELECT * FROM aggregated')
rows = cursor.fetchall()
#column_names = [description[0] for description in cursor.description]

#print(" | ".join(column_names))
#print("-" * 40)

#senti = 'sentiment'
#cursor.execute(f"SELECT * FROM coaches WHERE {senti} IS NOT NULL")

#rows = cursor.fetchall()

for row in rows:
    print(row)


#for row in rows:
#    pprint(row)

conn.close()

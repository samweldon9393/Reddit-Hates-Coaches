import sqlite3
#from pprint import pprint

left_group = ["Quin Snyder", "Erik Spoelstra", "Steve Clifford",
              "Billy Donovan", "Michael Malone", "Chris Finch", "Steve Kerr",
              "Rick Carlisle", "Taylor Jenkins", "Tom Thibodeau",
              "Mark Daigneault", "Nick Nurse", "Mike Budenholzer",
              "Gregg Popovich", "Darko Rajakovic", "Will Hardy",
              "Jordi Fernández", "Kenny Atkinson", "JJ Redick", "Brian Keefe"]
right_group = ["Joe Mazzulla", "Doc Rivers", "Adrian Griffin", "Jacque Vaughn",
               "J.B. Bickerstaff", "Jason Kidd", "Monty Williams", "Ime Udoka",
               "Tyronn Lue", "Darvin Ham", "Willie Green", "Jamahl Mosley",
               "Mike Brown", "Wes Unseld Jr", "Charles Lee","Chauncey Billups"]

conn = sqlite3.connect('coaches.db')
cursor = conn.cursor()

# Fetch all rows from the table
#cursor.execute('SELECT * FROM aggregated')
cursor.execute('SELECT coach, positive_count, negative_count from aggregated')
rows = cursor.fetchall()
#column_names = [description[0] for description in cursor.description]

#print(" | ".join(column_names))
#print("-" * 40)

#senti = 'sentiment'
#cursor.execute(f"SELECT * FROM coaches WHERE {senti} IS NOT NULL")

#rows = cursor.fetchall()

w_pos = 0
w_neg = 0
b_pos = 0
b_neg = 0

for row in rows:
    print(f"{row[0]} {row[1]} {row[2]}")

    '''
    coach = row[0]
    positive_count = row[1]
    negative_count = row[2]
    #print(row)
    if coach in left_group:
        w_pos += positive_count
        w_neg += negative_count
    elif coach in right_group:
        b_pos += positive_count
        b_neg += negative_count
    '''

print(f"b_pos = {b_pos} b_neg = {b_neg} w_pos = {w_pos} w_neg = {w_neg}")

#for row in rows:
#    pprint(row)

conn.close()

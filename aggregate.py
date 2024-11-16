import sqlite3

#Open the comments db
conn_src = sqlite3.connect('comments.db')
cursor_src = conn_src.cursor()

# Connect to or create the aggregated database
conn_dest = sqlite3.connect('coaches.db')
cursor_dest = conn_dest.cursor()

query = '''
    SELECT coach,
        SUM(CASE WHEN sentiment = 1 THEN 1 ELSE 0 END) AS pos,
        SUM(CASE WHEN sentiment = -1 THEN 1 ELSE 0 END) AS neg,
        COUNT(*) AS total
    FROM coaches
    GROUP BY coach
    ORDER BY coach
'''
# Create the results table if it doesn't already exist
cursor_dest.execute('''
CREATE TABLE IF NOT EXISTS aggregated (
    coach TEXT,
    mood TEXT,
    ratio REAL,
    positive_count INTEGER,
    negative_count INTEGER
)
''')
conn_dest.commit()
cursor_src.execute(query)
results = cursor_src.fetchall()

for name, pos, neg, total in results:
    mood = 'Neutral'
    if neg > pos:
        mood = 'Negative'
        if pos == 0:
            ratio = 100
        else:
            ratio = neg/pos * -1
    elif pos > neg:
        mood = 'Positive'
        if neg == 0:
            ratio = 100
        else:
            ratio = pos/neg * 1

    # Insert the results into the destination database
    cursor_dest.execute('''
        INSERT INTO aggregated (coach, mood, ratio, positive_count, negative_count)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, mood, ratio, pos, neg))

    #normalized_ratio = ratio / total

    #print(f"{name}: {mood}")
    #print(f" Ratio: {ratio:.2f}")
    #print(f" Positive count: {pos}")
    #print(f" Negative count: {neg}")
    #print(f" Normalized ratio: {normalized_ratio}")

conn_dest.commit()
conn_src.close()
conn_src.close()

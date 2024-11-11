import sqlite3

conn = sqlite3.connect('comments.db')
cursor = conn.cursor()

query = '''
    SELECT coach,
        SUM(CASE WHEN sentiment = 1 THEN 1 ELSE 0 END) AS pos,
        SUM(CASE WHEN sentiment = -1 THEN 1 ELSE 0 END) AS neg,
        COUNT(*) AS total
    FROM coaches
    GROUP BY coach
    ORDER BY coach
'''

cursor.execute(query)

results = cursor.fetchall()

for name, pos, neg, total in results:
    mood = 'Neutral'
    if neg > pos:
        mood = 'Negative'
        if pos is 0:
            ratio = 100
        else:
            ratio = neg/pos * -1
    elif pos > neg:
        mood = 'Positive'
        if neg is 0:
            ratio = 100
        else:
            ratio = pos/neg * 1

    normalized_ratio = ratio / total

    print(f"{name}: {mood}")
    print(f" Ratio: {ratio:.2f}")
    print(f" Positive count: {pos}")
    print(f" Negative count: {neg}")
    #print(f" Normalized ratio: {normalized_ratio}")

conn.close()

import numpy as np 
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

#turn the SQL database into a pandas matrix to perform calculations
conn = sqlite3.connect('comments.db')
cursor = conn.cursor()
query = 'SELECT * FROM coaches'
df = pd.read_sql_query(query, conn)

comment_counts = df['coach'].value_counts()
print(comment_counts)

#random sample from each coach
#grouped = df.groupby(['coach'])
#print(grouped.sample(1))

#checking what happened with Tibbs
tibbs = df[df['coach'] == 'Tom Thibodeau']
print(tibbs.sample(10))


import numpy as np 
import pandas as pd
import sqlite3

conn = sqlite3.connect('coaches.db')
cursor = conn.cursor()
query = 'SELECT * FROM aggregated'
df = pd.read_sql_query(query, conn)

print(df)

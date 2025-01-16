import numpy as np 
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

#turn the SQL database into a pandas matrix to perform calculations
conn = sqlite3.connect('coaches.db')
cursor = conn.cursor()
query = 'SELECT * FROM aggregated'
df = pd.read_sql_query(query, conn)
df.columns = ['Coach', 'Sentiment', 'Ratio', 'Positive', 'Negative']

#get the variance in the data set 
#find the distance of each ratio from the mean, save that in an array, square
#sum those and divide by number of data points to get variance

'''
ratio = np.array(df['Ratio'])
dists = ratio - np.mean(ratio)
sq_dists = dists ** 2
sum_sq_dists = sum(sq_dists)
variance = sum_sq_dists / len(df)
print(variance)
'''

#using built in functions
variance = np.var(df['Ratio'])
std = np.std(df['Ratio'])


print('Standard Deviation: ' + str(std))
print('variance: ' + str(variance))

print('\n\n')


iqr = np.quantile(df['Ratio'], .75) - np.quantile(df['Ratio'], .25)
print('IQR: ' + str(iqr))

lower = np.quantile(df['Ratio'], .25) - 1.5 * iqr
upper = np.quantile(df['Ratio'], .75) + 1.5 * iqr

print('lower: %s upper: %s' % (lower, upper))

outliers = df[(df['Ratio'] < lower) | (df['Ratio'] > upper)]

print(f'Outliers: {outliers}')

described = df['Ratio'].describe()
print('\n\nRatio collumn described: \n' + str(described))

all_described = df.describe()
print('\n\nWhole thing described: \n' + str(all_described))

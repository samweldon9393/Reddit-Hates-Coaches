import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3

# Connect to the database
conn = sqlite3.connect('coaches.db')  # Replace with your database
query = "SELECT coach, ratio FROM aggregated GROUP BY coach"
df = pd.read_sql_query(query, conn)

conn.close()

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

# Filter and sort each group by the y-value (ratio)
left_df = df[df['coach'].isin(left_group)].sort_values('ratio', ascending=False)
right_df = df[df['coach'].isin(right_group)].sort_values('ratio', ascending=False)

# Concatenate the two sorted groups
sorted_df = pd.concat([left_df, right_df])

# Set the category order
df['coach'] = pd.Categorical(df['coach'], categories=sorted_df['coach'], ordered=True)
# Sort the DataFrame by the custom order
df = df.sort_values('coach')

# Plot a bar graph
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='coach', y='ratio', hue='coach', dodge=False, legend=False)

# Customize the plot
plt.title('Ratio by Coach', fontsize=16)
plt.xlabel('Coach', fontsize=12)
plt.ylabel('Ratio', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.savefig('ordered_graph.png')
print("Graph saved as 'ordered_graph.png'")

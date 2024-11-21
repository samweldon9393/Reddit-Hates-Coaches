import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3

# Connect to the database
conn = sqlite3.connect('coaches.db')  # Replace with your database
query = "SELECT coach, ratio FROM aggregated GROUP BY coach"
df = pd.read_sql_query(query, conn)

conn.close()
'''
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
'''
age_order = ["Joe Mazzulla", "Will Hardy", "Mark Daigneault",
             "Charles Lee", "JJ Redick", "Taylor Jenkins", "Jordi Fernández",
             "Willie Green", "J.B. Bickerstaff", "Darko Rajakovic",
             "Jamahl Mosley", "Ime Udoka", "Adrian Griffin", "Chauncey Billups", 
             "Brian Keefe", "Wes Unseld Jr", "Jacque Vaughn", "Jason Kidd",
             "Darvin Ham", "Michael Malone", "Monty Williams", "Tyron Lue",
             "Erik Spoelstra", "Mike Brown", "Chris Finch", "Mike Budenholzer",
             "Kenny Atkinson", "Nick Nurse", "Quin Snyder", 
             "Billy Donovan", "Steve Kerr", "Doc Rivers", "Steve Clifford",
             "Rick Carlisle", "Tom Thibodeau", "Gregg Popovich"]
'''
# Filter and sort each group by the y-value (ratio)
left_df = df[df['coach'].isin(left_group)].sort_values('ratio', ascending=False)
right_df = df[df['coach'].isin(right_group)].sort_values('ratio', ascending=False)

# Concatenate the two sorted groups
sorted_df = pd.concat([left_df, right_df])

# Set the category order
df['coach'] = pd.Categorical(df['coach'], categories=sorted_df['coach'], ordered=True)
# Sort the DataFrame by the custom order
df = df.sort_values('coach')


tenure_order = [
    "JJ Redick", "Brian Keefe", "Charles Lee", "Jordi Fernández", "Kenny Atkinson", 
    "Adrian Griffin", "Darko Rajakovic",
    "Will Hardy", "Joe Mazzulla", "Darvin Ham", "Jamahl Mosley", "Willie Green", "Wes Unseld Jr.",
    "Ime Udoka", "Chauncey Billups", "Chris Finch", "Mark Daigneault", "Taylor Jenkins", "Nick Nurse",
    "Tyronn Lue", "Quin Snyder", "Billy Donovan", "Jacque Vaughn", "Steve Clifford", "Steve Kerr",
    "Mike Budenholzer", "Jason Kidd", "Michael Malone", "Tom Thibodeau", "Monty Williams", "Mike Brown",
    "Erik Spoelstra", "Rick Carlisle", "Doc Rivers", "Gregg Popovich"]
'''
# Filter the DataFrame to include only the relevant coaches
df = df[df['coach'].isin(age_order)]

# Set the category order using the custom list
df['coach'] = pd.Categorical(df['coach'], categories=age_order, ordered=True)

# Plot a bar graph
plt.figure(figsize=(10, 6))
#sns.barplot(data=df, x='coach', y='ratio', hue='coach', dodge=False, legend=False)
sns.lineplot(data=df, x='coach', y='ratio', marker='o', hue='coach', legend=False)

# Customize the plot
plt.title('Ratio by Coach (by Age)', fontsize=16)
plt.xlabel('Coach', fontsize=12)
plt.ylabel('Ratio', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.savefig('age_ordered_line_graph.png')
print("Graph saved as 'age_ordered_line_graph.png'")

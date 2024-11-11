#from nltk.sentiment.vader import SentimentIntensityAnalyzer
from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer
from names_lists import coaches
import sqlite3

#path to the directory with the LLM model in it
model_name = "distilbert-base-uncased-finetuned-sst-2-english"

# Load the model and tokenizer from the local directory
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
classifier = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)

'''
MAX_TOKEN_LENGTH = tokenizer.model_max_length
This is about 512, which I'm translating to about 1500 chars to be safe
'''

MAX_CHARS = 1500

#connect to the database
conn = sqlite3.connect('comments.db')
cursor = conn.cursor()
cursor.execute('SELECT id, comment, sentiment from coaches')
rows = cursor.fetchall()

#go through each db row
for row in rows:
    ID = row[0]
    comment = row[1]
    sentiment = row[2]
    
    #skip rows that already have a sentiment score
    if sentiment is None and len(comment) < MAX_CHARS:
        #Hugging Face lib classifies text as either POSITIVE or NEGATIVE
        #get those scores and save them as 1 or -1, 0 if score not generated
        sentiScore = classifier(comment)[0]['label']
        score = 0
        score = 1 if sentiScore == 'POSITIVE' else -1 if sentiScore == 'NEGATIVE' else 0
        
        #print to the terminal as we go just for fun
        print(score)
        
        #add the numerical scores into the database
        cursor.execute('''
            UPDATE coaches SET sentiment = ? WHERE id = ?
        ''', (score, ID))

conn.commit()
conn.close()


'''
SIA RULES BASED VERSION
I found this analysis did not work well on this data set
Leaving this code here as a comment for a reference if ever needed

senti = {}
sia = SentimentIntensityAnalyzer()

for coach in coaches:
    senti[coach] = [0, 0] #pos, neg

sia = SentimentIntensityAnalyzer()

with open('output_files/found_names.txt', 'r', encoding='utf-8') as file:
    for comment in file:
        for coach in coaches:
            if coach in comment:
                sentiment = sia.polarity_scores(comment)

                if sentiment['compound'] >= 0.05:
                    senti[coach][0] += 1

                elif sentiment['compound'] <= -0.05:
                    senti[coach][1] += 1

for key, value in senti.items():
    print(f"{key}: {value}")
'''    

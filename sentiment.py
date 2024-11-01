from nltk.sentiment.vader import SentimentIntensityAnalyzer
from names_lists import coaches

senti = {}

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

print(senti)

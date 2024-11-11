import sys
import praw
import sqlite3

#enforce argv usage
#file must be a list of Reddit thread IDs
if len(sys.argv) != 2:
    sys.exit("enter ID text file name as CLA")


#bring in data structurs that have the strings an substrings we're scraping for
from collections import defaultdict
from names_lists import names_dict
from names_lists import catch_coaches

#set up a Reddit instance with praw
reddit = praw.Reddit(client_id = 'Shfp5olKdH4lRQj2U33t1Q',
                     client_secret = 'rVCdH11KUEFiYkslES8GvR64R98jmg',
                     username = 'Downtown_Neat2620',
                     password = 'CoachesProject123',
                     user_agent = 'idk')
NBA_sub = reddit.subreddit('NBA')

#open up SQL connection to comments database
conn = sqlite3.connect('comments.db')
cursor  = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS coaches (
    id INTEGER PRIMARY KEY,
    coach TEXT NOT NULL,
    comment TEXT NOT NULL,
    sentiment INTEGER
)
''')
conn.commit()

#open up the file passed as 1st command line arg
with open(sys.argv[1], 'r', encoding='utf-8') as inFile:
    for line in inFile:
        #get an object for the Reddit post and pull each comments
        submission = reddit.submission(line)
        submission.comments.replace_more()

        for top_level_comment in submission.comments:
            comment_text = top_level_comment.body.lower();
            #first check if coach catcher substrings appear in comment
            if any(coach in comment_text for coach in catch_coaches):
                #if there, match to specific coach
                for name, nicknames in names_dict.items():
                    for nickname in nicknames:
                        #add into database
                        if nickname in comment_text:
                            cursor.execute('''
                            INSERT INTO coaches (coach, comment, sentiment) VALUES (?, ?, ?)
                            ''', (name, comment_text, None))
                            conn.commit()

conn.close()

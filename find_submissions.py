import praw

reddit = praw.Reddit(client_id = 'Shfp5olKdH4lRQj2U33t1Q',
                     client_secret = 'rVCdH11KUEFiYkslES8GvR64R98jmg',
                     username = 'Downtown_Neat2620',
                     password = 'CoachesProject123',
                     user_agent = 'idk')

NBA_sub = reddit.subreddit('NBA')

for submission in NBA_sub.top(limit=10000):
    #if submission.link_flair_itext != None and 'Game Thread' in submission.link_flair_text:
        #print(submission.title)
        #if (submission.link_falir_text != 'None'):
            #print(submission.link_flair_template_id)
        print(submission.id)

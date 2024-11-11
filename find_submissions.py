import praw

#set up a Reddit instance
reddit = praw.Reddit(client_id = 'Shfp5olKdH4lRQj2U33t1Q',
                     client_secret = 'rVCdH11KUEFiYkslES8GvR64R98jmg',
                     username = 'Downtown_Neat2620',
                     password = 'CoachesProject123',
                     user_agent = 'idk')

#swapped in r/NBA as well as each team's sub
NBA_sub = reddit.subreddit('NBASpurs')

#printing each game thread or post game thread id, gets redir to files
for submission in NBA_sub.search("Game Thread", limit=5000):
    print(submission.id)

import praw

reddit = praw.Reddit(client_id = 'Shfp5olKdH4lRQj2U33t1Q',
                     client_secret = 'rVCdH11KUEFiYkslES8GvR64R98jmg',
                     username = 'Downtown_Neat2620',
                     password = 'CoachesProject123',
                     user_agent = 'idk')

NBA_sub = reddit.subreddit('NBA')

#create an object for a specific post
submission = reddit.submission("1g8t97u")

submission.comments.replace_more(limit=0)
for top_level_comment in submission.comments:
    print(top_level_comment.body)

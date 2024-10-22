import praw

from names_lists import catch_coaches

reddit = praw.Reddit(client_id = 'Shfp5olKdH4lRQj2U33t1Q',
                     client_secret = 'rVCdH11KUEFiYkslES8GvR64R98jmg',
                     username = 'Downtown_Neat2620',
                     password = 'CoachesProject123',
                     user_agent = 'idk')

NBA_sub = reddit.subreddit('NBA')

#create an object for a specific post
submission = reddit.submission("1cyirss")

submission.comments.replace_more()
with open('output_comments_2.txt', 'w', encoding='utf-8') as file:
    for top_level_comment in submission.comments:
        comment_text = top_level_comment.body.lower();
        if any(coach in comment_text for coach in catch_coaches):
            file.write(comment_text + '\n')


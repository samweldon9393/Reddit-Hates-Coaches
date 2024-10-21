import praw

coaches = {"quin", "snyder", "mazzulla", "mazula", "mazzula", "mazulla", 
           " maz ", " mazz ", " doc ", "adrian", "griffin",
           "jacque", "vaughn", "vaugn", "clifford", "billy", "donovan",
           "j.b", "bickerstaff", " kidd ", "malone", "monty", "williams", 
           "finch", "kerr", " ime ", "udoka", "carlisle", "tyronn", "lue",
           "darvin", " ham ", "taylor", "jenkins", " spo ", "spoelstra", 
           "rivers", "willie green", "thibodeau", "thibbs", "tibbs", " tibs ", 
           "daigneault", "dagneault", "dagnault", "jamahl", "mosley", 
           "nurse", "budenholzer", " bud ", "chauncey", "billups", "mike brown",
           "coach brown", "coach mike", "gregg", "popovich", " pop ", "darko", 
           "rajakovic", "hardy", "wes", "unseld", "micah", "nori"}

reddit = praw.Reddit(client_id = 'Shfp5olKdH4lRQj2U33t1Q',
                     client_secret = 'rVCdH11KUEFiYkslES8GvR64R98jmg',
                     username = 'Downtown_Neat2620',
                     password = 'CoachesProject123',
                     user_agent = 'idk')

NBA_sub = reddit.subreddit('NBA')

#create an object for a specific post
submission = reddit.submission("1cfif4i")

submission.comments.replace_more()
with open('output_comments.txt', 'w', encoding='utf-8') as file:
    for top_level_comment in submission.comments:
        comment_text = top_level_comment.body.lower();
        if any(coach in comment_text for coach in coaches):
            file.write(comment_text + '\n')


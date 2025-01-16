-------------------------------------------------------------------------------
@author - Sam Weldon
@date - 11/16/2024

This is a collection of python scripts to scrape comments from r/NBA and the 
various NBA team subreddits, and then sort and analyze them.
-------------------------------------------------------------------------------

-----------------------------
Description of program parts:
-----------------------------

- aggregate.py - Used to aggregate the data from the SQLite database into
  analyzable form

- cleanup.py - Used to remove junk comments (such as comments about Blake
  Griffin that made it into Adrian Griffin's pool)

- find_submission.py - Used to generate lists of Submission IDs for posts on
  all of the NBA subreddits

- graph.py - Used to create graphs from the data

- names_lists.py - Used to collect data structures with coach names and comment
  catching substrings for nicknames and common misspellings

- scraper.py - Used to do the work of scraping the Reddit threads and sorting
  the found comments into the SQLite database

- sentiment.py - Used for performing the sentiment analysis

- sort.py - Used early in the project for testing sorting, this functionality
  wound up being included in scraper.py

- sql_print.py - Used to print the SQLite databases to the terminal

-------------------------------------------------------------------------------

--------------------
METHODOLOGY WRITE UP
--------------------

I wrote a collection of Python programs that scraped around 7,750
Reddit threads and collected just south of 100,000 comments that each featured
the name of at least one NBA head coach. Each comment was sorted and stored in
a database. I then graded each comment with
a sentiment score of either “positive” or “negative.” I aggregated those data, made
a few graphs, and looked for trends. I chose to use Reddit comments instead of
some other social media for two reasons: First, Reddit comments are very easy
to scrape. I would love to repeat this experiment with Instagram or Twitter/X
content, but collecting that data would be more difficult. The other
reason is that Reddit users are very likely to be young white men who identify
as liberal (Pew). Given that a subset of the white male population who
self-identify as liberal are likely to profess anti-racist views, this data set
may be particularly revealing of the effects of unconscious bias.

To collect the data, I used the
PRAW Python library which works with Reddit API to allow all sorts of
functionality, including comment scraping. The data set was all of the
posts titled  “Game Thread” or “Post Game Thread” from each NBA team’s
subreddit as well as the main NBA subreddit (the automated search was able to
scrape around 250 threads from each sub). The comments were sorted by
coach and entered into an SQLite database. I then used the pre-trained
natural language processing model from Hugging Face's Transformers library to
perform sentiment analysis on each comment. Finally, I used the
Pandas, Matplotlib, and Seaborn libraries to create graphs from the data
(included below).

Being constrained by time, my relatively novice Python skills,
and most of all the technical hurdles of working on my little Acer laptop,
the data collection and analysis methods had several severe limitations and
shortcomings. For instance, the data sets for some coaches are much larger than
others, resulting partially from coaches' names. Gregg Popovich is frequently
called “Pop,” but attempting to collect those comments would have meant
attributing to him every comment about how some player is “about to pop off,”
etc. There were a few such examples. Furthermore, a comment like “I hate Jason
Kidd, he’s a horrible idiot, glad we have Mike Brown,” would be considered
negative, and attributed to both Kidd and Brown, even though it is in fact
positive about Brown. I won’t spend any more time here discussing these
shortcomings, except to say that the saving grace is that most of the data
collection issues are equally true for all of the coaches in the study, and
the sample size should be large enough that the effects of this noise are
minimized.

-------------------------------------------------------------------------------

-------
RESULTS
-------

b_pos = 13494 b_neg = 41484 w_pos = 10934 w_neg = 27744

The actual SQL databases are on GitHub so anyone can verify the numbers without
having to run all of these scripts again. Overall, the findings are interesting
and seem to suggest that there may be evidence of bias against black head
coaches. This data collection method is too primitive to make any sweeping
claims about these findings, but I do think the sample size is relevant enough
to claim that it demonstrates a need for further analysis.

Here's what I found:

- Overall, there were 16 black head coaches included in this study and 20
  coaches who were not considered black for this purpose.
- On average, black head coaches received negative comments 2.63x more often
  than positive comments
- On average, non-black coaches received negative comments 2.04x more often than
  positive comments.
- This represents a ~25% increase in negative comment frequency for black head
  coaches when compared with their non-black counterparts.
- There were a few outliers that distorted the data somewhat.
  - Kenny Atkinson had the best reception of any coach in the study, one of only
    two to have a positive ratio of positive to negative comments. However,
    during the time period this data covers, he was mostly an assistant coach,
    and has only head coached ~10 games (and his Caveliers won every single one
    of them).
  - Jordi Fernández had also only head coached ~10 games when this sample was
    taken. He was the other coach with a positive ratio. It's likely that
    there's some new coach shine affecting his results, and I expect his ratio
    to come down as his Nets face an almost certainly losing season. Still, the
    general sentiment among observers seems to be that he is a wunderkind,
    holding a PhD in sport psychology and, hailing from Spain, he is
    representative of a modern European basketball strategy ideology that is 
    viewed favorably by the stat nerd type who frequents Reddit (I think this is
    likely a closely related phenomenon to the bias this research is studying).
  - Darvin Ham's bar on the graph nearly shoots off the bottom of the screen,
    being the only coach to even approach, let alone surpass a ratio of 4/1
    negative to positive comments (final count was -4.1x). Ham coached in the
    notoriously difficult LA media market, and his Lakers underachieved at least
    by some standards (though they did reach the West Finals and win the
    inaugural In-Season Tournament). I do think the anti-black coach bias this
    research is focused on has a lot to do with Ham's negative perception
    (especially when compared to the positive reception his replacement, JJ
    Reddick has already received), but the LA market factor is certainly very
    important, and Reddick has not coached enough games to compare yet.
- For the reasons outlined above, I also crunched the numbers after removing
  those three statistical outliers.
  - Without Ham, black coaches had a ratio of 2.53/1 negative to positive, and
    without Atkinson and Fernández, non-black head coaches had a ratio of
    2.38/1. That's a less statistically significant difference, and it gets at
    the limits of this study. Even with nearly 100,000 comments, the sample was
    inconsistent. However, I left this comment as more of an after thought
    because I think removing those coaches obscures too much. Darvin Ham was
    loathed by Lakers fans on Reddit, but there's no reason to think we can
    eliminate racial bias as a cause for that loathing. Attkinson and Fernández
    both had smaller sample sizes due to coahcing less games, but so did Charles
    Lee, who racked up a negative ratio in the same amount of games. Adrian
    Griffin only coached half a season in this sample and his ratio was firmly
    negative at 3/1.
- Statistical Significance
  - This data set illustrates that Group B had a ratio of negative-to-positive
    comments around 25% higher than that ratio for Group A. However, BOTH groups
    recieved overwhelmingly more negative comments than positive, with 75% of
    Group B's overall comments being negative, and 72% for Group A. That is a
    difference of around 3.2%, but thanks to the large sample size, we can say
    with relative confidence that both the difference in the ratios and the
    difference in the proportions of comments are statistically significant
  


- Who went in which
  category was based on general perception, as this study is concerned with
  commenters' bias, so their perception is ultimately what mattered. The data
  is available if anyone wants to see how things shake out with differently
  constructed categories.

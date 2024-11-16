-------------------------------------------------------------------------------
@author - Sam Weldon
@date - 11/16/2024

This is a collection of python scripts to scrape comments from r/NBA and the 
various NBA team subreddits, and then sort and analyze them.
-------------------------------------------------------------------------------

-------
RESULTS
-------

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

  Who went in which
  category was based on general perception, as this study is concerned with
  commenters' bias, so their perception is ultimately what mattered. The data
  is available if anyone wants to see how things shake out with differently
  constructed categories.


-----
TODO:
-----
  Need to go through and refilter a few of the coaches
    Jacque Vaughn caught Jamie Jacquez comments
     - DONE
    Adrian Griffin caught Blake Griffin comments
     - DONE
    Mike Malone caught Karl Malone
     - DONE


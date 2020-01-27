---
layout: default
---
<!---
Text can be **bold**, _italic_, or ~~strikethrough~~.

[Link to another page](./another-page.html)

There should be whitespace between paragraphs.

There should be whitespace between paragraphs. We recommend including a README, or a file with information about your project.
--->
# The Mamba Mentality

Kobe Bryant capped off his Hall of Fame career by scoring 60 points against the Utah Jazz at home. He did so in
exactly 50 field goal attempts. In this respect, that last game serves as a perfect microcosm of Kobe’s 20 seasons
in the league; an elite scorer unmatched by anyone at his prime, and an unabashed gunslinger never hesitant to
let it fly from almost anywhere on the court. It was no coincidence that Kobe was the highest volume perimeter
shooter in the history of the game with 26200 attempts, surpassed only by elite inside players Karl Malone (26210)
and Kareem Abdul-Jabbar (28307). It is, therefore, instructive to take a closer look at Kobe’s shot selection
patterns and their results. In particular we will address the question of the hot hand, the idea that field goal
percentage increases following a hot streak of made shots. Via a Markov Chain Model, we demonstrate that past
shots had little notable effect on Kobe’s percentages. In this way, we argue that Kobe Bryant’s confidence was a
manifestation of the memoryless property of his shooting.

### What Hot Hand?
Kobe was renowned for going on streaks where he looked unstoppable. This hot hand theory is wildly popular,
applied to virtually any NBA player who makes a few shots in a row, and no doubt the casual player has experienced
that sensation of confidence at the local gym. But do these assumptions hold weight when we analyse Kobe’s
numbers?
Let’s examine how different aspects of Kobe’s game change with his attempts. If the criticisms are true,
and Kobe just jacked up bad shots even when he was in a funk, we could expect a higher number of attempts
to correlate with a lower percentage. Alternatively, if the field percentage increases with attempts, then some
credence could be given to the theory. Here is Kobe’s FG percentage vs FG attempted – in the following charts
the 2013-14 season has been dropped since he only played 6 games:

![fig1](./kobe/fig1.png)
{:.image-caption}
*<center>Kobe Bryant FGA vs FG%.</center>*

There certainly some positive correlation, but this itself is not completely conclusive. It could be that more made
shots simply give more confidence and result in a better shooting percentage. Correlation, however does not imply
causation so this itself is not conclusive. What it does say, however is that we should pursue a further exploration
of the numbers to look for the hot hand effect.
Up till now we have not made much distinction between 2 point and 3 point field goals, so let’s compare FGA vs
True Shooting Percentage. We use TS% This accounts for the fact that a 3 pointer is worth more and accordingly
contributes more to the percentage:

![fig2](./hobe/fig2.png)
{:.image-caption}
*<center>Kobe Bryant FGA vs TS%.</center>*



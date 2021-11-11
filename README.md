# Republicans vs Democrats

## Abstract (150 words)

Donald Trump's election in 2017 was only one illustration of the Left-Right political cleavage in the United States of America, USA. Leveraging the Quotebank dataset, the project idea would be to measure the evolution of this cleavage across time, and especially focus on how major elections i.e. the presidential election or midterms affect the cleavage short-term. We're expecting this cleavage to increase, specially around events such as the presidential election or some specific events like the outbreak of the corona epidemic (2020), major mass shootings [1], the first impeachment of Trump (2019), the riot in Charlottesville (2017). We are not looking at events from 2021, and hence, the January 6th riots and Joe Biden taking office are omitted.
The political cleavage will be measured through a sentiment analysis over the quotes from contemporary political members of the republican and democtratic parties targeting members of the other party.


## Research Questions

How did the political cleavage in the US evolve during the last 5 years ?
Did some specific events (presidential elections, midterms, outbreak of the corona virus, etc.) have any impact on the cleavage ?
Which politicians are the least aggresive and which are the most aggressive ?
Does the political party correlate with being more or less aggresive ?
Can the time-series of data points from the sentiment analysis fit well to a function from which the trend and uncertainty can be described. 

Additional questions if time permits:
What are the most used terms ?
How is the lexical richness and how does it develop over time ?

## Proposed additional datasets

We've extracted the members of the US congress from the Biographical Directory of the United States Congress https://bioguide.congress.gov that have been active in last 14 years.

## Methods

Firstly, four people (Timothy Johnson, Donald Payne, Duncan Hunter and Patrick Murphy) in the list congress members appear twice for various reasons. For instance, Timothy Johnsons district was redrawn giving him two entries and Donald Payne refer to two different politicians (Donald M. Payne and Donald Payne Jr. - father and son), but they are both democrats. This should not affect our analysis if we just drop the duplicates. 
In order to observe the evolution in political cleavage, we've decided to first extract quotes expressed by members of the congress dataset. Then, out of these quotes, extract the ones mentionning members of the opposition. And, from the latter, apply a sentiment analysis process to assess the positivity and negativity scores which we translate as a measure of degree of cleavage between the 2 parties. Comparing these measures or the distribution of scores over time could inform us on the evolution of this cleavage.

## Proposed timeline

- Sentiment analysis on quotes
- - Calculate sentiment for each quote
- - Descriptive analysis (trends, plots, statistics, etc.)
- - Analyse around key events mentioned earlier. Presidential elections, midterms, etc.
- - Regression or similar on the time-series
- - Compare republicans to democrats
- - Who are the most and least aggressive speakers
- - Possibly try another sentiment meausure and compare with previous results.
- - - Are the results stable across measures
- - - Is irony influencing the results
- Make webpage with these results and ensure this is on track before continuing

- Analyse frequently used terms
- Lexical analysis on quotes
- - Find measure for lexical richness
- - Calculate lexical richness for each quote
- - Descriptive analysis (trends, plots, statistics, etc.)
- - Regression or similar on the time-series
- - Compare republicans to democrats

## Organization within the team

(Deadline: Dec 17)
Task - Person responsible - Deadline (23:59 on the date)

- Calculate sentiment for quotes resulting in two time-series for initial sentiment measure - Daryna - November 18
- Descriptive analysis of sentiment - Andreas - November 18
- Analyse around key events - René - November 21
- Compare republicans to democrats - Olivier - November 21
- Find least and most aggressive speakers - Olivier - November 21
- Regression on time-series - Andreas - November 21
- Try another sentiment measure - Daryna - November 24
- Analyse results with new measure - René - November 28
- Starting webpage with story - Olivier - November 28
- Inserting results from sentiment analysis - All w.r.t. their previous area of responsibility - December 8
- Analyse frequently used terms and inserting the results - any if time permits - December 12
- Lexical richness and inserting results - any if time permits - December 12


## Questions for TAs 


## References
[1] Wikipedia contributors. (2021, November 9). List of mass shootings in the United States. In Wikipedia, The Free Encyclopedia. Retrieved 10:17, November 11, 2021, from https://en.wikipedia.org/w/index.php?title=List_of_mass_shootings_in_the_United_States&oldid=1054289389

# Republicans vs Democrats

## Abstract (150 words)

Trump's election in 2017 was only one illustration of the increasing Left-Right political cleavage in the US. Leveraging the Quotebank dataset, the project idea would be to measure the evolution of this cleavage across time. We're expecting this cleavage to increase, specially around events such as the presidential election or some specific events (corona, mass shootings, impeachment, Trump wall..)
This cleavage will be measured through a sentiment analysis over the quotes from contemporary political members of the republican and democtratic parties. This analysis' results will be compared over different periods...

## Research Questions

How did the political cleavage in the US evolve during the last 5 years ?
Did some specific event (presidential election..) have any impact on the cleavage ?
Are some politicians more aggressive than others ?

## Proposed additional datasets

We've extracted the members of the US congress from the Biographical Directory of the United States Congress https://bioguide.congress.gov that have been active in last years 14 years.

## Methods

In order to observe the evolution in political cleavage, we've decided to first extract quotes expressed by members of the congress dataset. Then, out of these quotes, extract the ones mentionning members of the opposition. And, from the latter, apply a sentiment analysis process to assess the positivity and negativity scores which we translate as a measure of degree of cleavage between the 2 parties. Comparing these measures or the distribution of scores over time could inform us on the evolution of this cleavage.

## Proposed timeline

2015 to 2020 (phase E), as the data from quotebank from this period is the best extracted one (the capitalization kept and non-ASCII characters properly represented).   

## Organization within the team

Olivier has done a good job in finding and extracting members of the congress then 
Olivier : congress members and extraction, extraction of quotes and work on 
Rene : help on extraction of quotes mentionning the opposition, search of a good sentiment analysis and first implementation, formatting the notebook
Daryna : work on the quotes extraction and application of the sentiment analysis over the whole data
Andreas : extracting the quotes and the speaker attributes, more inc

TODO :
EDA
Look for best sentiment analysis
Try advanced SA to take care of irony, or look for patterns and ways to manually take care of it
Check issues on some mentions (Trump family mentionned instead of Donald..)
Quotes preprocessing ?
Compare the SA/cleavage scores and distributions, statistical test on evolution, increase ?




## Questions for TAs 



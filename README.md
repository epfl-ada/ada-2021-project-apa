# Republicans vs Democrats

## Abstract 

Donald Trump's election in 2017 was only one illustration of the Left-Right political cleavage in the United States of America, USA. Leveraging the Quotebank dataset, the project idea would be to measure the evolution of this cleavage across time, and especially focus on how major elections i.e. the presidential election or midterms affect the cleavage short-term. We're expecting this cleavage to increase, specially around events such as the presidential election or some specific events like the outbreak of the corona epidemic (2020), major mass shootings [1], the first impeachment of Trump (2019), the riot in Charlottesville (2017). We are not looking at events from 2021, and hence, the January 6th riots and Joe Biden taking office are omitted.
The political cleavage will be measured through a sentiment analysis over the quotes from contemporary political members of the republican and democratic parties targeting members of the other party.

## Research Questions

How did the political cleavage in the US evolve during the last 5 years ?
Did some specific events (presidential elections, midterms, outbreak of the corona virus, etc.) have any impact on the cleavage ?
Which politicians are the least aggressive and which are the most aggressive ?
Does the political party correlate with being more or less aggressive ?
Can the time-series of data points from the sentiment analysis fit well to a function from which the trend and uncertainty can be described. 

Additional questions if time permits:
What are the most used terms ?
How is the lexical richness and how does it develop over time ?

## Proposed additional datasets

We've extracted the members of the US congress from the Biographical Directory of the United States Congress https://bioguide.congress.gov that have been active in last 14 years.

## Methods

As explained, we are interested in the political cleavage between Right and Left in the US, measured by their sentiment score. In order to do that, we decided to limit ourselves to the 2015 to 2020 timeframe. Below is a detailed explanation of the different methods and steps we take to analyze that.

### 1. Data extraction	
_The relevant notebook for this part is called **data_extraction.ipynb**._
First of all, we need to have a dataset to work on. From the Quotebank 2015-2020 dataset, we need to extract the quotes expressed by US politicians. We decided to limit ourselves to the members of the US congress, to which we manually added Donald Trump (the President is not a congress member). Given the size of the data, each quotebank yearly dataset was split into chunks, on which we extracted data. 

Once we had all quotes from congress members (and Donald Trump), we then extracted only the quotes that where mentioning any congress member of the other party. For example, we extracted the following quote from Trump (a republican) because he was mentioning Hillary Clinton (a democrat):
> With Hillary Clinton, i said: 'be at my wedding, '

The following figure illustrates the data pipeline:
![Data pipeline](figures/data_pipe.png)

Remarks:
- For now, we decided to naively extract quotes, meaning that we simply detect when the speaker is the exact name (Name + Family Name) of a politician. For the next milestone, we want to implement a less-naive approach by also capturing aliases of politicians.
- Some politicians appear numerous times in the congress members list for various reasons. For instance, Donald Payne refer to two different politicians (Donald M. Payne and Donald Payne Jr. - father and son). For now, we decided to drop those "duplicates" and not retrieve their quotes. This could be changed in a future version of our work.

### 2. Political cleavage analysis
_The relevant notebook for this part is called **sentiment_eda.ipynb**._
From the above final dataset, we want to analyze the political cleavage accross time. As previously said, we simply compute their sentiment score in order to do that. Currently, we are using NLTK's vader sentiment scorer [2]. This algorithm analyzes the words in a given sentence, and compares it against a dictionary of positive and negative words. It is quite advanced in the sense that it handles score boosting given numerous factors, for example punctuation (adding multiple exlamation marks) or using all caps. 

Using the computed scores, we then analyze its evolution accross time for the two parties. For now, you can see some exploratory data analysis in the relevant notebook.

Remarks:
- Preliminary analyses show that most quotes are classified as "neutral". We will need to investigate if this seems to be correct.
- One of the reason for the above remark is that we preprocessed the quotes to easily detect mentions of policians. Namely, we made all the quotes lowercase, scrapping some information that could be used by the sentiment algorithm.

## Proposed timeline

- Sentiment analysis on quotes
    - Calculate sentiment for each quote
    - Descriptive analysis (trends, plots, statistics, etc.)
    - Analyse around key events mentioned earlier. Presidential elections, midterms, etc.
    - Regression or similar on the time-series
    - Compare republicans to democrats
    - Who are the most and least aggressive speakers
    - Possibly try another sentiment measure and compare with previous results.
        - Are the results stable across measures
        - Is irony influencing the results
- Make webpage with these results and ensure this is on track before continuing
- Analyse frequently used terms
- Lexical analysis on quotes
    - Find measure for lexical richness
    - Calculate lexical richness for each quote
    - Descriptive analysis (trends, plots, statistics, etc.)
    - Regression or similar on the time-series
    - Compare republicans to democrats

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
[2] https://www.nltk.org/_modules/nltk/sentiment/vader.html

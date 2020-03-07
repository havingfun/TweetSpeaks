TweetSpeaks
===========

Twitter Sentiment Analyzer in Django

Twitter Sentiment Analysis has been performed on tweets that are extracted live from twitter using Python-Twitter API.

![Screenshot](https://github.com/havingfun/TweetSpeaks/blob/master/TweetSpeaks.png)
[Live Demo](https://radiant-forest-9929.herokuapp.com/)

I have used existing codes and tried to work on them, tried to improve the accuracy. I used three methods -
1. Naive Bayes - Poor Accuracy
I used training data set of Movie Reviews from nltk.github.io/nltk_data/

2. Max Entropy - Poor Accuracy
I used training data set of Movie Reviews from nltk.github.io/nltk_data/

3. Polarity Score - Good Accuracy
I used two files pos.txt and neg.txt to check the positive and negative scores of the tweets and on the basis of scores, sentiments were analyzed.

#For Future
a) Mapping of ShortWords -
   osum - Awesome
b) Bigram Classifiers

For extracting live tweets one change has to be done in - TweetSpeaks_1.0\tweetsentiments\TwitterSentimentAnalysis\searchtweets.py
We have to replace -
api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
with some authentic keys.

Then we can start the project by
python manage.py runserver

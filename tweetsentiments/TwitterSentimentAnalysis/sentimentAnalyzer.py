from preprocess_tweet import *
from filtering_tweets import *
from searchtweets import searchtweetsbykeyword
from polarity_test import polarity_test
import csv
import nltk
import pprint
import os
cwd = os.path.dirname(os.path.abspath(__file__))
#Read the tweets one by one and process it
inpTweets = csv.reader(open(cwd+'/'+'data/trainerMedium.csv', 'rb'), delimiter=',', quotechar='|')
tweets = []
def getFeatureList(fileName):
    fp = open(fileName, 'r')
    line = fp.readline()
    featureList = []
    while line:
        line = line.strip()
        featureList.append(line)
        line = fp.readline()
    fp.close()
    return featureList
featureList = getFeatureList(cwd+'/'+'data/trainedFeatureListMedium.txt')
final = []
for row in inpTweets:
	sentiment = row[0]
	tweet = row[1]
	processedTweet = processTweet(tweet)
	featureVector = getFeatureVector(processedTweet)
	final = final+list(set(featureVector))
	tweets.append((featureVector, sentiment));
#fh = open("data/trainedFeatureListSmall.txt", "w")
#fh.write(str(final))
print 'Done Training'
#print tweets
def extract_features(tweet):
    tweet_words = set(tweet)
    features = {}
    for word in featureList:
        features['contains(%s)' % word] = (word in tweet_words)
    return features
training_set = nltk.classify.util.apply_features(extract_features, tweets)
pp = pprint.PrettyPrinter()
#pp.pprint(training_set)
# Train the classifier
NBClassifier = nltk.NaiveBayesClassifier.train(training_set)

MaxEntClassifier = nltk.classify.maxent.MaxentClassifier.train(training_set, 'GIS', trace=3, \
encoding=None, labels=None, sparse=True, gaussian_prior_sigma=0, max_iter = 10)

print 'Done Classification'

def analyze(keyword):
	tweetstream = searchtweetsbykeyword(keyword)
	tweetsent = []
	for testTweet in tweetstream:
		entry = []
		testTweet = testTweet.encode('ascii', 'xmlcharrefreplace')
		entry.append(testTweet)
		processedTestTweet = processTweet(testTweet)
		#print processedTestTweet
		sentiment = NBClassifier.classify(extract_features(getFeatureVector(processedTestTweet)))
		entry.append(sentiment)
		#print "By Naive Bayes - Sentiment = %s\n" % (sentiment)
		#tokens = nltk.word_tokenize(processedTestTweet)
		#postagged = nltk.pos_tag(tokens)
		#processedTestTweet = ""
		#for pair in postagged:
		#		if(pair[1]=='JJ' or pair[1]=='NN'):
		#			processedTestTweet = processedTestTweet + pair[0]
		sentiment =  MaxEntClassifier.classify(extract_features(getFeatureVector(processedTestTweet)))
		entry.append(sentiment)
		#print "By Maximum Entropy - Sentiment = %s\n" % (sentiment)
		sentiment = polarity_test(processedTestTweet)
		#print "By Polarity Score - Sentiment = %s\n" % (sentiment)
		entry.append(sentiment)
		tweetsent.append(entry)
	return tweetsent
'''while(1):
	keyword = raw_input()
	if(keyword=="quit"): break
	tweetstream = searchtweetsbykeyword(keyword)
	for testTweet in tweetstream:
		testTweet = testTweet.encode('ascii', 'xmlcharrefreplace')
		processedTestTweet = processTweet(testTweet)
		print processedTestTweet
		sentiment = NBClassifier.classify(extract_features(getFeatureVector(processedTestTweet)))
		print "By Naive Bayes - Sentiment = %s\n" % (sentiment)
		#tokens = nltk.word_tokenize(processedTestTweet)
		#postagged = nltk.pos_tag(tokens)
		#processedTestTweet = ""
		#for pair in postagged:
		#		if(pair[1]=='JJ' or pair[1]=='NN'):
		#			processedTestTweet = processedTestTweet + pair[0]
		sentiment =  MaxEntClassifier.classify(extract_features(getFeatureVector(processedTestTweet)))
		print "By Maximum Entropy - Sentiment = %s\n" % (sentiment)
		sentiment = polarity_test(processedTestTweet)
		print "By Polarity Score - Sentiment = %s\n" % (sentiment)
'''
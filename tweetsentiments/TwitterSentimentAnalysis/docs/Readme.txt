Training Sets Used -
http://www.cs.cornell.edu/people/pabo/movie-review-data
There are sets of positive and negative reviews.
Collection of Positive Adjectives and Negative Adjectives
Just go through all the files and train the classifier
 
Functions Used to Train the -
training_set = nltk.classify.util.apply_features(extract_features, tweets)

Function Used to Classify the Data on Basis of Naive Bayes Theorem
sentiment = NBClassifier.classify(extract_features(getFeatureVector(processedTestTweet, stopWords)))
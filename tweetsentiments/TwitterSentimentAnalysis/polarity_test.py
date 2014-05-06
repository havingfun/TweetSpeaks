from sentiments_dict import *
import os
cwd = os.path.dirname(os.path.abspath(__file__))
def polarity_test(tweet):
	tweet = tweet.lower()
	words = tweet.split(" ")
	wc = len(words)
	pos = 0
	neg = 0
	fp = open(cwd+"/"+"data/pos.txt", "r")
	fn = open(cwd+"/"+"data/neg.txt", "r")
	data = fp.readlines()
	poswords = data[0].split(" ")
	data = fn.readlines()
	negwords = data[0].split(" ")
	for nw in words:
		fl = 0
		for xc in poswords:
			if(nw==xc):
				pos = pos+1
				fl = 1
				break
		if(fl==0):
			for xc in negwords:
				if(nw==xc):
					neg = neg+1
					break
	'''cat, dic = read_file('resources/LIWC2007_English080730.dic')
	poswords, negwords = get_wordsets(dic)
	for nw in words:
		fl = 0
		for xc in poswords:
			if xc[-1] == "*":
				if nw.startswith(xc[:-1]):
						pos = pos+1
						fl = 1
						break
			else:
				if(nw==xc):
					pos = pos+1
					fl = 1
					break
		for xc in negwords:
			if xc[-1] == "*":
				if nw.startswith(xc[:-1]):
						pos = pos+1
						fl = 1
						break
			else:
				if(nw==xc):
					pos = pos+1
					fl = 1
					break
	'''
	print pos,neg
	if pos > neg: return 'positive'
	if pos < neg: return 'negative'
	return 'neutral'
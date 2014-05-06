import time
import string
import os
cwd = os.path.dirname(os.path.abspath(__file__))
def read_file(filename):
    data = open(filename, "r")
    mode = 0
    cat = {}
    dic = {}
    for line in data:
        line = line.strip("\r\n")
        if line == "%":
            mode += 1
            continue
        elif mode == 1:
            chunks = line.split("\t")
            cat[chunks[0]] = chunks[1]
        elif mode == 2:
            chunks = line.split("\t")
            word = chunks.pop(0)
            dic[word] = chunks
    return (cat,dic) # cat = list of categories, dic = list of all words with categories
	
# read in dictionary and partition it into set of positive and negative word
def get_wordsets(dic):
    poswords = []
    negwords = []
    for word in dic:
        for cat in dic[word]:
            if cat in ['126']:
                poswords.append(word)
                continue
        for cat in dic[word]:
            if cat in ['19', '127', '128', '129', '130']:
                negwords.append(word)
                continue
    return (poswords, negwords)

cat, dic = read_file(cwd+'/'+'resources/LIWC2007_English080730.dic')
poswords, negwords = get_wordsets(dic)
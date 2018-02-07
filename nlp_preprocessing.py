from nltk import word_tokenize
import stopwords
import json
import re
import pandas as pd
import unicodedata
import nltk

sentence = "this is a foo bar sentence"

emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""

regex_str = [
    emoticons_str,
    r'<[^>]+>',  # HTML tags
    r'(?:@[\w_]+)',  # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",  # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',  # URLs

    r'(?:(?:\d+,?)+(?:\.?\d+)?)',  # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])",  # words with - and '
    r'(?:[\w_]+)',  # other words
    r'(?:\S)'  # anything else
]

tokens_re = re.compile(r'(' + '|'.join(regex_str) + ')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^' + emoticons_str + '$', re.VERBOSE | re.IGNORECASE)


def tokenize(s):
    return tokens_re.findall(s)


def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens

print(preprocess(sentence))

stop = set(stopwords.get_stopwords('english'))
#stop = set(stopwords.words('english'))

tweets_data_path = '/Users/priyamurthy/Documents/PycharmProjects/program1/twitter_data.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet['text'])
    except:
        continue
print 'Im here'
#i=0
#while i<len(tweets_data):
 #   print([i for i in tweets_data[i].lower().split() if i not in stop])

print([i for i in sentence.lower().split() if i not in stop])
#print([i for i in tweets_data.lower().split() if i not in stop])

print len(tweets_data)
tweets = pd.DataFrame()

#tweets['text'] = list(map(lambda tweet: tweet['text'], tweets_data))
print len(tweets_data)

#tweets['text'] = list(map(lambda x:x.lower(),tweets['text']))



#print(tweets['text'])

print 'Done'
#tweets['text'] = map(lambda tweet:tweet['text'].,tweets_data)
i = 0
data = []
while i < len(tweets_data):
    #print(tweets_data[i])
    preprocess(tweets_data[i],True)
    print([unicodedata.normalize('NFKD', j).encode('ascii', 'ignore') for j in tweets_data[i].lower().split() if j not in stop])
    #print
    i += 1

#print data

#for key,value in tweets_data.items():

#for j in tweets_data:
 #   for i
  #  print([i for i in j.lower().split() if i not in stop]






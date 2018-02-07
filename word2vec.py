import tensorflow as tf
import json
import pandas as pd
import matplotlib.pyplot as plt
import re
import nltk
import gensim
from nltk import word_tokenize
import stopwords
from nltk import word_tokenize
import unicodedata
import nltk
nltk.download('punkt')

#filename = '/Users/priyamurthy/Documents/PycharmProjects/program1/twitter_data.txt'
filename   ='/Users/priyamurthy/Documents/twitter_data1.txt'
#filename = '/Users/priyamurthy/Documents/temp_data.txt'

stop = set(stopwords.get_stopwords('english'))

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


tweets_data = []
tweets_file = open(filename, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue



print len(tweets_data)



tweets = pd.DataFrame()


tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)
tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)

tweets_by_lang = tweets['lang'].value_counts()




def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False


tweets['flu'] = tweets['text'].apply(lambda tweet: word_in_text('flu', tweet))
tweets['fever'] = tweets['text'].apply(lambda tweet: word_in_text('fever', tweet))
tweets['cough'] = tweets['text'].apply(lambda tweet: word_in_text('cough', tweet))

temp_data = []
for line in tweets_file:
    try:
        tweet = json.loads(line)
        temp_data.append(tweet['text'])
    except:
        continue
i=0
print 'Im here'
while i< len(temp_data):
   temp_data[i] = temp_data[i].lower()
   print temp_data[i]



x = tweets['text'].values.tolist()
print x


corpus = x

tok_corp = [nltk.word_tokenize(sent, 'english') for sent in corpus]
print tok_corp
print type(tok_corp)
#words = [w.lower() for word in text.split() for text in tok_corp]
words = []
for text in tok_corp:
    for word in text:
        temp = word.lower()
        words.append(unicodedata.normalize('NFKD', temp).encode('ascii', 'ignore') )

#print words
#print words

model = gensim.models.Word2Vec(tok_corp, min_count=1, size=2)

print model

#print model.most_similar('influenza')


print 'flu', model['flu']

print 'fever',model['fever']

print 'cold', model['cold']

print 'cough' ,model['cough']


print 'feeling', model['feeling']

print 'so' ,model['so']


print 'miserable', model['miserable']

print 'having' ,model['having']


print 'a', model['a']

print 'flu' ,model['flu']

print 'fever', model['fever']

print 'did' ,model['did']

print 'not', model['not']

print 'go' ,model['go']

print 'to', model['to']

print 'school' ,model['school']

print 'i', model['i']

print 'will' ,model['will']

print 'stay', model['stay']

print 'at' ,model['at']

print 'home', model['home']

print 'do' ,model['do']

print 'some', model['some']

print 'gentle' ,model['gentle']

print 'stretching', model['stretching']

print 'and' ,model['and']

print 'nourish', model['nourish']

print 'myself' ,model['myself']

print 'with', model['with']

print 'herbal' ,model['herbal']

print 'teas', model['teas']

print 'or' ,model['or']

print 'veggie', model['veggie']

print 'juices' ,model['juices']

print model.most_similar('flu')

#data = []
#for line in corpus:
 #   try:
  #      for word in line.split():
   #         print word , model[word]
    #    print 'Next tweet'

    #except:
     #   continue

#print len(data)

#i = 0
#while i < len(tweets_data):
    #print(tweets_data[i])
 #   print([unicodedata.normalize('NFKD', j).encode('ascii', 'ignore') for j in tweets_data[i].lower().split() if j not in stop])
    #print
  #  i += 1


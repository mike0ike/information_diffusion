# -*- coding: utf-8 -*-
# Use Python 2.6+
# python my_twitter.py ../../../../keywords_politics_us.txt
# ALL STRINGS SHOULD BE HANDLED AS UTF-8!

from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import skfuzzy
import skfuzzy.control as ctrl

class FuzzyModule:
    def __init__ (self, followersStart=0, followersStop=10, tweetTextStart=1, tweetTextStop=280, popularityStart=0, popularityStop=1000):
        self.__followersStart = followersStart
        self.__followersStop = followersStop
        self.__tweetTextStart = tweetTextStart
        self.__tweetTextStop = tweetTextStop
        self.__popularityStart = popularityStart
        self.__popularityStop = popularityStop

    def setFollowersLowStart(self, start):
        self.__followersLowStart = start

    def setFollowersLowMid(self, mid):
        self.__followersLowMid = mid

    def setFollowersLowStop(self, stop):
        self.__followersLowStop = stop

    def setFollowersModStart(self, start):
        self.__followersModStart = start

    def setFollowersModMid(self, mid):
        self.__followersModMid = mid

    def setFollowersModStop (self, stop):
        self.__followersModStop = stop

    def setFollowersHighStart(self, start):
        self.__followersHighStart = start

    def setFollowersHighMid(self, mid):
        self.__followersHighMid = mid

    def setFollowersHighStop(self, stop):
        self.__followersHighStop = stop

    def setFollowersLow(self, start, mid, stop):
        self.setFollowersLowStart(start)
        self.setFollowersLowMid(mid)
        self.setFollowersLowStop(stop)

    def setFollowersMod(self, start, mid, stop):
        self.setFollowersModStart(start)
        self.setFollowersModMid(mid)
        self.setFollowersModStop(stop)

    def setFollowersHigh(self, start, mid, stop):
        self.setFollowersHighStart(start)
        self.setFollowersHighMid(mid)
        self.setFollowersHighStop(stop)

    def setFollowers(self, lowStart, lowMid, lowStop, modStart, modMid, modStop, highStart, highMid, highStop):
        self.setFollowersLow(lowStart, lowMid, lowStop)
        self.setFollowersMod(modStart, modMid, modStop)
        self.setFollowersHigh(highStart, highMid, highStop)

    def setTweetTextLowStart(self, start):
        self.__tweetTextLowStart = start

    def setTweetTextLowMid(self, mid):
        self.__tweetTextLowMid = mid

    def setTweetTextLowStop(self, stop):
        self.__tweetTextLowStop = stop

    def setTweetTextModStart(self, start):
        self.__tweetTextModStart = start

    def setTweetTextModMid(self, mid):
        self.__tweetTextModMid = mid

    def setTweetTextModStop(self, stop):
        self.__tweetTextModStop = stop

    def setTweetTextHighStart(self, start):
        self.__tweetTextHighStart = start

    def setTweetTextHighMid(self, mid):
        self.__tweetTextHighMid = mid

    def setTweetTextHighStop(self, stop):
        self.__tweetTextHighStop = stop

    def setTweetTextLow(self, start, mid, stop):
        self.setTweetTextLowStart(start)
        self.setTweetTextLowMid(mid)
        self.setTweetTextLowStop(stop)

    def setTweetTextMod(self, start, mid, stop):
        self.setTweetTextModStart(start)
        self.setTweetTextModMid(mid)
        self.setTweetTextModStop(stop)

    def setTweetTextStop(self, start, mid, stop):
        self.setTweetTextHighStart(start)
        self.setTweetTextHighMid(mid)
        self.setTweetTextHighStop(stop)

    def setTweetText(self, lowStart, lowMid, lowStop, modStart, modMid, modStop, highStart, highMid, highStop):
        self.setTweetTextLow(lowStart, lowMid, lowStop)
        self.setTweetTextMod(modStart, modMid, modStop)
        self.setTweetTextStop(highStart, highMid, highStop)

    def setPopularityLowStart(self, start):
        self.__popularityLowStart = start

    def setPopularityLowMid(self, mid):
        self.__popularityLowMid = mid

    def setPopularityLowStop(self, stop):
        self.__popularityLowStop = stop

    def setPopularityModStart(self, start):
        self.__popularityModStart = start

    def setPopularityModMid(self, mid):
        self.__popularityModMid = mid

    def setPopularityModStop(self, stop):
        self.__popularityModStop = stop

    def setPopularityHighStart(self, start):
        self.__popularityHighStart = start

    def setPopularityHighMid(self, mid):
        self.__popularityHighMid = mid

    def setPopularityHighStop(self, stop):
        self.__popularityHighStop = stop

    def unPopular(self, start, mid, stop):
        self.setPopularityLowStart(start)
        self.setPopularityLowMid(mid)
        self.setPopularityLowStop(stop)

    def midPopular(self, start, mid, stop):
        self.setPopularityModStart(start)
        self.setPopularityModMid(mid)
        self.setPopularityModStop(stop)

    def veryPopular(self, start, mid, stop):
        self.setPopularityHighStart(start)
        self.setPopularityHighMid(mid)
        self.setPopularityHighStop(stop)

    def setPopularity(self, lowStart, lowMid, lowStop, modStart, modMid, modStop, highStart, highMid, highStop):
        self.unPopular(lowStart, lowMid, lowStop)
        self.midPopular(modStart, modMid, modStop)
        self.veryPopular(highStart, highMid, highStop)

    def makeVariables (self):
        """
            step 1: create input, output variables
        :return:
        """
        self.__followers = ctrl.Antecedent(np.arange(self.__followersStart, self.__followersStop), "FOLLOWERS")
        self.__tweetText = ctrl.Antecedent(np.arange(self.__tweetTextStart, self.__tweetTextStop), "TWEETTEXT")
        self.__popularity = ctrl.Consequent(np.arange(self.__popularityStart, self.__popularityStop), "POPULARITY")

    def makeMemberFunctions (self):
        """
            step 2: create member functions
        :return:
        """
        self.__followers["small"] = skfuzzy.trimf( self.__followers.universe,
                                                 [self.__followersLowStart, self.__followersLowMid,
                                                  self.__followersLowStop] )
        self.__followers["medium"] = skfuzzy.trimf( self.__followers.universe,
                                                      [self.__followersModStart, self.__followersModMid,
                                                       self.__followersModStop] )
        self.__followers['high'] = skfuzzy.trimf( self.__followers.universe,
                                                  [self.__followersHighStart, self.__followersHighMid,
                                                   self.__followersHighStop] )

        self.__tweetText["small"] = skfuzzy.trimf( self.__tweetText.universe,
                                                   [self.__tweetTextLowStart, self.__tweetTextLowMid,
                                                    self.__tweetTextLowStop] )
        self.__tweetText['medium'] = skfuzzy.trimf( self.__tweetText.universe,
                                                    [self.__tweetTextModStart, self.__tweetTextModMid,
                                                     self.__tweetTextModStop] )
        self.__tweetText['high'] = skfuzzy.trimf( self.__tweetText.universe,
                                                  [self.__tweetTextHighStart, self.__tweetTextHighMid,
                                                   self.__tweetTextHighStop] )

        self.__popularity["small"] = skfuzzy.trimf(self.__popularity.universe,
                                                   [self.__popularityLowStart, self.__popularityLowMid,
                                                    self.__popularityLowStop])
        self.__popularity["medium"] = skfuzzy.trimf( self.__popularity.universe,
                                                    [self.__popularityModStart, self.__popularityModMid,
                                                     self.__popularityModStop])
        self.__popularity["high"] = skfuzzy.trimf( self.__popularity.universe,
                                                    [self.__popularityHighStart, self.__popularityHighMid,
                                                     self.__popularityHighStop])

    def makeRules(self):
        """
            step 3: create fuzzy rules
        :return:
        """
        rule1 = ctrl.Rule( self.__followers["small"] & self.__tweetText["small"], self.__popularity["small"])
        rule2 = ctrl.Rule( self.__followers["small"] & self.__tweetText["medium"], self.__popularity["small"])
        rule3 = ctrl.Rule( self.__followers["small"] & self.__tweetText["high"], self.__popularity["medium"])

        rule4 = ctrl.Rule( self.__followers["medium"] & self.__tweetText["small"], self.__popularity["small"])
        rule5 = ctrl.Rule( self.__followers["medium"] & self.__tweetText["medium"], self.__popularity["medium"])
        rule6 = ctrl.Rule( self.__followers["medium"] & self.__tweetText["high"], self.__popularity["medium"] )

        rule7 = ctrl.Rule( self.__followers["high"] & self.__tweetText["small"], self.__popularity["high"])
        rule8 = ctrl.Rule( self.__followers["high"] & self.__tweetText["medium"], self.__popularity["high"])
        rule9 = ctrl.Rule( self.__followers["high"] & self.__tweetText["high"], self.__popularity["high"])

        """
            step 4: create a control system
        """
        self.__rules = []
        for i in range(1, 10):
            self.__rules.append(eval("rule" + str(i)))

        self.__popularityCtrl = ctrl.ControlSystem(self.__rules)
        self.__popularityCtrl.view()


    def simulate(self, followersVal, tweetTextLong):
        """
        :param followersVal: number of followers
        :param tweetTextLong: number of signs in text message
        :return: res: a string store step by step instructions how the fuzzy controler infer
        res is stored in result.txt
        """
        popularityCtrlSil = ctrl.ControlSystemSimulation( self.__popularityCtrl )
        popularityCtrlSil.input["FOLLOWERS"] = followersVal
        popularityCtrlSil.input["TWEETTEXT"] = tweetTextLong
        popularityCtrlSil.compute()

        self.result = popularityCtrlSil.print_state()
        self.output = popularityCtrlSil.output.items()[0][1]

        # def getResult():
        #     outputFile = open("result.txt", "r")
        #     return outputFile.read()
        #
        # getResult()
        print(popularityCtrlSil.output)
        print(self.result)




###########################################################################################################################################
import pandas as pd
import numpy as np
import logging
import gensim
import bokeh.plotting as bp
from bokeh.models import HoverTool
from bokeh.plotting import figure, show, output_notebook
from gensim.models.word2vec import Word2Vec
from tqdm import tqdm
from nltk.tokenize import TweetTokenizer
from sklearn.manifold import TSNE
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from keras.models import Sequential
from keras.layers import Activation, Dense
from sklearn.preprocessing import scale
from copy import deepcopy
from string import punctuation
from random import shuffle

# Shows status bar
tqdm.pandas(desc="progress-bar")
# Gendsim model
LabeledSentence = gensim.models.doc2vec.LabeledSentence
# Tweet tokenizer from nltk
tokenizer = TweetTokenizer()
pd.options.mode.chained_assignment = None
# Tool for logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


def dataHandler(filename):
    data = pd.read_csv(filename, header=None)
    data.drop([1, 2, 3, 4], axis=1, inplace=True)
    data = data.rename(columns={0: 'Sentiment'})
    data = data.rename(columns={5: 'SentimentText'})


    data = data[data.Sentiment.isnull() == False]
    #data['Sentiment'] = data['Sentiment'].map(int)

    #assert isinstance(data, int)
    data['Sentiment'] = data['Sentiment'].map({4:1, 0:0})
    data = data[data['SentimentText'].isnull() == False]
    data.reset_index(inplace=True)
    data.drop('index', axis=1, inplace=True)
    return data

# noinspection PyBroadException
def myTokenize(tweet):
    try:
        tweet = unicode(tweet.decode('utf-8').lower())
        tokens = tokenizer.tokenize(tweet)
        tokens = filter(lambda t: not t.startswith('@'), tokens)
        tokens = filter(lambda t: not t.startswith('#'), tokens)
        tokens = filter(lambda t: not t.startswith('http'), tokens)
        return tokens
    except:
        return 'NC'


def postprocessData(data, n=1000000):
    data = data.head(n)
    data['tokens'] = data['SentimentText'].progress_map(myTokenize)
    data = data[data.tokens != 'NC']
    data.reset_index(inplace=True)
    data.drop('index', inplace=True, axis=1)
    return data


def labelizeTweets(tweets, label_type):
    labelized = []
    for i, v in tqdm(enumerate(tweets)):
        label = '{}_{}'.format(label_type, i)
        labelized.append(LabeledSentence(v, [label]))
    return labelized


def buildWord2Vector(tokens, size, tweet_w2v=None, tfidf=None):
    vec = np.zeros(size).reshape((1, size))
    count = 0
    for word in tokens:
        try:
            vec += tweet_w2v[word].reshape((1, size)) + tfidf[word]
            count += 1
        except KeyError:
            continue
    if count != 0:
        vec /= count
    return vec


def main():

    # filename = './trainingandtestdata/testdata.manual.2009.06.14.csv'
    filename = '/home/mike/Desktop/data_set/trainingandtestdata/trainingandtestdata/training.1600000.processed.noemoticon.csv'

    nProb = 1000000
    nDim = 200

    data = dataHandler(filename)
    data = postprocessData(data, nProb)

    xTrain, xTest, yTrain, yTest = train_test_split(np.array(data.head(nProb).tokens), np.array(data.head(nProb).Sentiment), test_size=0.2)
    xTrain = labelizeTweets(xTrain, 'TRAIN')
    xTest = labelizeTweets(xTest, 'TEST')

    tweetW2V = Word2Vec(size=nDim, min_count=10)
    tweetW2V.build_vocab([x.words for x in tqdm(xTrain)])
    tweetW2V.train([x.words for x in tqdm(xTrain)], total_examples=tweetW2V.corpus_count, epochs=tweetW2V.iter)



    #print(tweetW2V.wmdistance())

    print("len: ")
    print(xTrain[0])
    print(len(xTrain[0]))

    print()
    'building tf-idf matrix ...'
    vectorizer = TfidfVectorizer( analyzer=lambda x: x, min_df=10 )
    matrix = vectorizer.fit_transform( [x.words for x in xTrain] )
    tfidf = dict( zip( vectorizer.get_feature_names(), vectorizer.idf_ ) )
    print()
    'vocab size :', len( tfidf )

    def buildWordVector (tokens, size):
        vec = np.zeros( size ).reshape( (1, size) )
        count = 0.
        for word in tokens:
            try:
                vec += tweetW2V[word].reshape( (1, size) )*tfidf[word]
                count += 1.
            except KeyError:  # handling the case where the token is not
                # in the corpus. useful for testing.
                continue
        if count != 0:
            vec /= count
        return vec

    from sklearn.preprocessing import scale
    train_vecs_w2v = np.concatenate( [buildWordVector( z, nDim ) for z in tqdm( map( lambda x: x.words, xTrain ) )] )
    train_vecs_w2v = scale( train_vecs_w2v )

    test_vecs_w2v = np.concatenate( [buildWordVector( z, nDim ) for z in tqdm( map( lambda x: x.words, xTest ) )] )
    test_vecs_w2v = scale( test_vecs_w2v )

    model = Sequential()
    model.add( Dense( 32, activation='relu', input_dim=200 ) )
    model.add( Dense( 1, activation='sigmoid' ) )
    model.compile( optimizer='rmsprop',
                   loss='binary_crossentropy',
                   metrics=['accuracy'] )

    model.fit( train_vecs_w2v, yTrain, epochs=9, batch_size=32, verbose=2 )

    score = model.evaluate( test_vecs_w2v, yTest, batch_size=128, verbose=2 )
    print(score[1])



    #for i in xrange(len(xTrain)):
     #   print(xTrain[i])
        # fuzzyModule.setFollowers(10,  10, 50,  10,  50,  100, 50,  100, 250)
         # fuzzyModule.setTweetText(10, 50, tweetW2V.vector_size(xTrain[i]), 100, 150, tweetW2V.vector_size(xTrain[i + 1]), 100, 150, tweetW2V.vector_size(xTrain[i + 2]))
        # fuzzyModule.setPopularity( 10, 20, 30, 40, 50, 60, 70, 80, 90 )
        # fuzzyModule.makeVariables()
        # fuzzyModule.makeMemberFunctions()
        # fuzzyModule.makeRules()
      #  print()
        #print(tweetW2V.vector_size(xTrain[i]))

        # fuzzyModule.simulate(50, tweetW2V.vector_size(xTrain[i]))

    #print(tweetW2V)

    print(tweetW2V['good'])
    print(len(tweetW2V['good']))
    print()
    print(tweetW2V.most_similar('good'))
    print(len(tweetW2V.most_similar( 'good')))
    print()
    print(tweetW2V.most_similar('bar'))
    print(len(tweetW2V.most_similar( 'bar' ) ))
    print()

    #print(tweetW2V.most_similar('facebook'))
    #print(tweetW2V.most_similar('iphone'))
    #
    # fuzzyModule = FuzzyModule(0, 35, 10, 50)
    # fuzzyModule.setFollowers(0,  10, 50,  10,  50,  100, 50,  100, 250)
    # fuzzyModule.setTweetText(10, 50, (len(tweetW2V['good'])), 100, 150, (len(tweetW2V['good'])), 150, 200, (len(tweetW2V['good'])))
    # fuzzyModule.setPopularity(10, 20, 30, 40,  50,  60,  70,  80, 90)
    #
    # fuzzyModule.makeVariables()
    # fuzzyModule.makeMemberFunctions()
    # fuzzyModule.makeRules()
    #
    # fuzzyModule.simulate(50, 240)

    # defining the chart
    # output_notebook()
    # plotTfidf = bp.figure(plot_width=700, plot_height=600, title="A map of 10000 word vectors",
    #                       tools="pan,wheel_zoom,box_zoom,reset,hover,previewsave",
    #                       x_axis_type=None, y_axis_type=None, min_border=1)
    #
    # # getting a list of word vectors. limit to 10000. each is of 200 dimensions
    # word2Vectors = [tweetW2V[w] for w in tweetW2V.wv.vocab[:5000]]
    #
    # # dimensionality reduction. converting the vectors to 2d vectors
    # tsneModel = TSNE(n_components=2, verbose=1, random_state=0)
    # tsneW2V = tsneModel.fit_transform(word2Vectors)
    #
    # # putting everything in a dataframe
    # tsneDf = pd.DataFrame(tsneW2V, columns=['x', 'y'])
    # tsneDf['words'] = tweetW2V.wv.vocab[:5000]
    #
    # # plotting. the corresponding word appears when you hover on the data point.
    # plotTfidf.scatter(x='x', y='y', source=tsneDf)
    # hover = plotTfidf.select(dict(type=HoverTool))
    # hover.tooltips = {"word": "@words"}
    # figure()
    # show(plotTfidf)

    # if True:
    #     print 'building tf-idf matrix ...'
    #     #vectorTfidf = TfidfVectorizer(analyzer=lambda x_vec:x_vec, min_df=10)
    #     vectorTfidf = TfidfVectorizer(analyzer= lambda x: x, min_df=10)
    #     # matrix = vectorizer.fit_transform([x.words for x in xTrain])
    #     tfidf = dict(zip(vectorTfidf.get_feature_names(), vectorTfidf.idf_))
    #     print 'vocab size :', len(tfidf)
    #
    #     trainVectorW2V = np.concatenate([buildWord2Vector(z, nDim) for z in tqdm(map(lambda x_train:x_train.words, xTrain))])
    #     print(trainVectorW2V)
    #     trainVectorW2V = scale(trainVectorW2V)
    #
    #     testVectorW2V = np.concatenate([buildWord2Vector(z, nDim) for z in tqdm(map(lambda x_test:x_test.words, xTest))])
    #     testVectorW2V = scale(testVectorW2V)
    #
    #     model = Sequential()
    #     model.add(Dense(32, activation='relu', input_dim=200))
    #     model.add(Dense(1, activation='sigmoid'))
    #
    #     model.add(Activation(32, activation='relu', input_dim=200))
    #     model.add(Activation(1, activation="sigmoid"))
    #
    #     model.compile(optimizer='rmsprop',
    #                   loss='binary_crossentropy',
    #                   metrics=['accuracy'])
    #
    #     model.fit( trainVectorW2V, yTrain, epochs=20, batch_size=32, verbose=2 )
    #
    #     result = model.evaluate(testVectorW2V, yTest, batch_size=128, verbose=2)
    #     print result[1]


if __name__ == '__main__':
    main()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 09:24:58 2020
SentiArt1.0.py basic sentiment analysis tool for literary texts
@author: ajacobs@zedat.fu-berlin.de
"""
# get packages
import os,codecs
import pandas as pd
import nltk
from nltk import*
import matplotlib.pyplot as plt


""" get the table with sentiment values (e.g., AAPz, fear_z). 
these are based on a vector space model (w2v, skipgram, 300d) and the label list published in:
https://www.frontiersin.org/articles/10.3389/fnhum.2017.00622/full#supplementary-material; https://www.frontiersin.org/articles/10.3389/fpsyg.2020.574746/full
the values for each word are: AAPz,ang_z,fear_z,disg_z,hap_z,sad_z,surp_z
they provide the affective-aesthetic potential (AAP) and discrete emotion values (anger, fear, disgust, sadness and surprise), all standardized (z-values), 
for each word, based on their semantic relatedness (as computed by w2v) with labels (semantic anchors) described in the publications mentioned in readme.md
"""

TC = '250kSentiArt_EN.xlsx' # for English texts
#TC = '120kSentiArt_DE.xlsx' # for German texts
sa = pd.read_excel(TC) #           

# open a short sample text
#fn = 'momo_4s.txt' # GERMAN
fn = 'harry.txt' # ENGLISH
with codecs.open(fn,'r','utf-8') as f:
    raw = f.read().replace('\n',' ').replace('\r','').replace('!',' ')  
sents = sent_tokenize(raw)
tokens = [[t for t in word_tokenize(s) if t.isalpha()] for s in sents]

#compute mean AAP (or mean fear etc.) per sentence
sent_mean_AAPz = [];sent_mean_fear_z = []
for t in tokens:
    dt = sa.query('word in @t')
    sent_mean_AAPz.append(dt.AAPz.mean())
    sent_mean_fear_z.append(dt.fear_z.mean())

#panda & save results
df = pd.DataFrame()
df['sent'] = tokens
df['AAPz'] = sent_mean_AAPz
df['fear_z'] = sent_mean_fear_z
df = round(df,3)
#df.to_csv('results.txt')

#plot AAPz, fear_z etc.
df.set_index(df.index,inplace=True)
df.plot(kind='bar',alpha=0.75, rot=0)
plt.xlabel("Sentence #")
plt.ylabel("Sentiment Value (z)")
plt.show()

#get most beautiful and ugliest words in corpus
topb = sa.sort_values(by=['AAPz']).tail()
print('top beauty words','\n',topb.word)
print()
topu = sa.sort_values(by=['AAPz']).head()
print('top ugly words','\n',topu.word)

#get most beautiful and fearful sents in text
print('top AAP sent','\n',df.sort_values(by=['AAPz']).tail(1))
print()
print('top FEAR sent','\n',df.sort_values(by=['fear_z']).tail(1))


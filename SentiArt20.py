#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 09:24:58 2020
SentiArt20.py basic sentiment analysis tool for literary texts
@author: ajacobs@zedat.fu-berlin.de
"""
# get packages
import os,codecs
import pandas as pd
import nltk
from nltk import *

# open a short sample text
fn = 'momo_4s.txt'
with codecs.open(fn,'r','utf-8') as f:
    raw = f.read().replace('\n',' ')

# get the table with sentiment values. they are based on a vector space model (w2v, skipgram, 300d) and the label list published in:
# https://www.frontiersin.org/articles/10.3389/fnhum.2017.00622/full#supplementary-material; https://www.frontiersin.org/articles/10.3389/fpsyg.2020.574746/full
# the values for each word are: AAPz,ang_z,fear_z,disg_z,hap_z,sad_z,surp_z
# they provide the affective-aesthetic potential (AAP) and discrete emotion values (anger, fear, disgust, sadness and surprise), all standardized (z-values), 
# for each word, based on their semantic relatedness (as computed by w2v) with labels (semantic anchors) described in the publications mentioned in readme.md

TC = '120kSentiArt_DE.xlsx' # for German texts
#TC = '250kSentiArt_EN.xlsx' # for English texts
sa = pd.read_excel(TC, index_col=0)                     
sents = sent_tokenize(raw)
tokens = [word_tokenize(s) for s in sents]

#compute mean AAPz (or mean ang_z etc.) per sentence
sent_mean_AAPz = []
for t in tokens:
    dt = sa.query('wordUC in @t')
    sent_mean_AAPz.append(dt.AAPz.mean())
# print results
for s,aapz in zip(sents,sent_mean_AAPz):
    print(s,round(aapz,3))
# save results as pandas df
df = pd.DataFrame()
df['sent'] = sents
df['AAPz'] = sent_mean_AAPz
df.to_csv('results.txt')

#plot AAPz
df.AAPz.hist()

#plot AAPz
df.AAPz.hist()

df.set_index(df.index,inplace=True)
df.plot(kind='bar',alpha=0.75, rot=90)
plt.xlabel("Sentence #")
plt.show()              

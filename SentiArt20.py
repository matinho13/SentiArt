#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 09:24:58 2020
SentiArt20.py basic SA for özdemir ipynb !!!!
@author: ajacobs@zedat.fu-berlin.de
"""

import os,codecs
import pandas as pd
import nltk
from nltk import *

fn = 'momo_4s.txt'
with codecs.open(fn,'r','utf-8') as f:
    raw = f.read()
#for Orange
#with open(fn.split('.')[0], 'w',encoding='utf8') as f:json.dump(raw, f, indent=4) 
#with open(fn.split('.')[0], 'r') as f:xxx = json.load(f)                    

TC = '120kSentiArt_DE.xlsx'
sa = pd.read_excel(TC, index_col=0)                     
sents = sent_tokenize(raw)
tokens = [word_tokenize(s) for s in sents]

sent_mean_AAPz = []
for t in tokens:
    dt = sa.query('wordUC in @t')
    sent_mean_AAPz.append(dt.AAPz.mean())

for s,aapz in zip(sents,sent_mean_AAPz):
    print(s,round(aapz,3))



              
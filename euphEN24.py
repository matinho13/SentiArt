#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 10:01:03 2024
@author: arthurjacobs
"""
import re, numpy as np

def euphEN23(w):
    """ heuristic computing simplified 
    sonority score for English based
    on graphemes """
    w = w.lower()
    exceptions = ['caretaker','latecomer','lonesome','sometimes'] # work in progress !!!
    seg = ['a.e','e.e','i.e','o.e','u.e','a.es','e.es','i.es','o.es','u.es'] # 5 silent e patterns
    sc = []
    lw = len(w)
    gr = ['a','â','à','á','e','ê','è','é','o','ô','ò','i','u','j','w','y','r','l','m','n','z','v','f','h','s','b','d','g','x','c','k','q','p','t','µ']
    va = [10,10,10,10,9,9,9,9,9,9,9,8,8,8,8,8,7,6,5,5,4,4,3,3,3,2,2,2,2,1,1,1,1,1,0]   
    for i in range(len(w)):
        if w[i] in gr:
            idx = gr.index(w[i])
            sc.append(va[idx])
    ssc = sum(sc)
#   if syllapy.count(w) == 1: # drop silent e for monosyls
    for s in seg: 
        if re.search(s, w) and (w.endswith('e') or w.endswith('es')) \
        and w not in exceptions:
            ssc = ssc - 9
    if w.endswith('ence'):ssc = ssc - 9 # SCIENCE, FENCE etc.. work in progress
    SC = ssc / np.mean(lw)
    SC2 = ssc / np.sqrt(lw)
    return w, round(SC,2)

euphEN23('piss') # 3.75
euphEN23('pee') # 6.33




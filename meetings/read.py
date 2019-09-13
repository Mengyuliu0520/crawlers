# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 19:02:27 2018

@author: Mengyu Liu
"""
import pandas as pd
import classifer 
p = open('author.txt','r',encoding='utf-8')
k = p.readlines()
nodup = list(set(k))
authors = [s.strip('\n') for s in nodup]
au = pd.DataFrame({'Author':authors})
gcf = classifer.GenderClassifier()
gcf.model_train()
# gcf.feature_set()
print(gcf.gender_classifier('mi yang'))
print(gcf.informative_features())


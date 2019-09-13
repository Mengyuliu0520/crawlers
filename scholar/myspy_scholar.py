# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 11:00:59 2018

@author: Mengyu Liu
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
import time

class PaperItem(object):
    Title = ''
    Authors = []

class Getpaper(object):
    def __init__(self):
        self.urls = []
        self.items = []
        
    def getHTMLText(self,url):
        try:
            r = requests.get(url, timeout=30)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            return r.text
        except:
            return ""
  
    def getUrls(self):
        self.urls = ['https://scholar.google.com/citations?user=NDrCCokAAAAJ']
        
    def spider(self):
        dest = open('papers.txt', 'w',encoding='utf-8')
        i = 0
        for url in self.urls:
            item = PaperItem()
            htmlContent = self.getHTMLText(url)
            soup = BeautifulSoup(htmlContent,'lxml')
            titles = soup.find_all('a',attrs={'class':'gsc_a_at'})
            print(titles)
            '''authors = authors_part.find_all('li',attrs={'class':'author'})
            au_str = ''
            for author in authors:
                name = author.getText()
                item.Authors.append(name+'\n')
                au_str = au_str+'$'+name
            self.items.append(item)
            print(soup.title.getText())
            print(au_str)
            dest.write(soup.title.getText()+'\n')
            dest.write(au_str+'\n')
            i = i+1'''
    
    def author_pool(self):
        pool = []
        for item in self.items:
            this = item.Authors
            print(this)
            pool=pool+this
        return pool

    
if __name__ == '__main__':
    start = time.time()
    GP = Getpaper()
    GP.getUrls()
    GP.spider()
    '''au_pool = GP.author_pool()
    k = open('author.txt', 'w',encoding='utf-8')
    k.writelines(au_pool)
    au = pd.DataFrame({'Author':au_pool})
    au.to_csv('author.csv', sep='\t', encoding='utf-8')
    print('It took {0:0.1f} seconds'.format(time.time() - start))'''

